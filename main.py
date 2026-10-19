from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

BASE_DIR = Path(__file__).resolve().parent
USERS_FILE = BASE_DIR / "users.csv"
SONGS_FILE = BASE_DIR / "songs.csv"
VALID_MOODS = {"happy", "sad", "calm", "energetic", "romantic", "roadtrip"}


def load_users():
    if not USERS_FILE.exists():
        raise FileNotFoundError(
            "users.csv was not found. Copy users.example.csv to users.csv first."
        )
    df = pd.read_csv(USERS_FILE, dtype=str).fillna("")
    required = {"Username", "Password"}
    if not required.issubset(df.columns):
        raise ValueError("users.csv must contain Username and Password columns.")
    df["Username"] = df["Username"].str.strip()
    df["Password"] = df["Password"].str.strip()
    return df


def load_songs():
    if not SONGS_FILE.exists():
        raise FileNotFoundError("songs.csv was not found in the project folder.")
    df = pd.read_csv(SONGS_FILE).fillna("")
    if not {"Mood", "Song"}.issubset(df.columns):
        raise ValueError("songs.csv must contain Mood and Song columns.")
    df["Mood"] = df["Mood"].astype(str).str.strip().str.lower()
    df["Song"] = df["Song"].astype(str).str.strip()
    return df


def login():
    try:
        users = load_users()
    except (FileNotFoundError, ValueError) as error:
        print(f"Setup error: {error}")
        return False

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    # Demo-only login. Plain-text password storage is not secure for real applications.
    match = (users["Username"] == username) & (users["Password"] == password)
    if match.any():
        print("Login successful!")
        return True
    print("Invalid username or password.")
    return False


def add_user():
    try:
        users = load_users()
    except (FileNotFoundError, ValueError) as error:
        print(f"Could not load users: {error}")
        return

    while True:
        username = input("Enter new username: ").strip()
        password = input("Enter new password: ").strip()
        if not username or not password:
            print("Username and password cannot be empty.")
        elif users["Username"].eq(username).any():
            print("User already exists.")
        else:
            users.loc[len(users)] = [username, password]
            users.to_csv(USERS_FILE, index=False)
            print("New user added.")
        if input("Add another user? (y/n): ").strip().lower() != "y":
            break


def recommend_songs():
    moods = load_songs()
    while True:
        mood = input(
            "Enter mood (happy, sad, calm, energetic, romantic, roadtrip): "
        ).strip().lower()
        matches = moods[moods["Mood"] == mood]
        if not matches.empty:
            print(f"\nSongs for mood '{mood}':")
            for number, song in enumerate(matches["Song"], start=1):
                print(f"{number}. {song}")
        else:
            print("Mood not found. Check the available categories and try again.")
        if input("Try another mood? (y/n): ").strip().lower() != "y":
            break


def view_categories():
    songs = load_songs()
    moods = sorted(mood for mood in songs["Mood"].unique() if mood)
    print("\nAvailable mood categories:")
    for mood in moods:
        print(f"- {mood}")


def add_song():
    songs = load_songs()
    while True:
        mood = input("Enter mood for the new song: ").strip().lower()
        song = input("Enter song name (optionally: Song Title by Singer): ").strip()
        if not mood or not song:
            print("Mood and song name cannot be empty.")
        else:
            new_row = pd.DataFrame([{"Mood": mood, "Song": song}])
            songs = pd.concat([songs, new_row], ignore_index=True)
            songs.to_csv(SONGS_FILE, index=False)
            print("Song added successfully.")
        if input("Add another song? (y/n): ").strip().lower() != "y":
            break


def remove_song():
    songs = load_songs()
    while True:
        print("\nExisting songs:")
        print(tabulate(songs, headers="keys", tablefmt="rounded_grid", showindex=False))
        song_to_remove = input("Enter the exact song name to remove: ").strip()
        matches = songs["Song"].str.casefold() == song_to_remove.casefold()
        if matches.any():
            songs = songs.loc[~matches].reset_index(drop=True)
            songs.to_csv(SONGS_FILE, index=False)
            print("Song removed successfully.")
        else:
            print("Song not found.")
        if input("Remove another song? (y/n): ").strip().lower() != "y":
            break


def show_all_songs():
    songs = load_songs()
    print("\nAll songs in the database:\n")
    print(tabulate(songs, headers="keys", tablefmt="fancy_grid", showindex=False))


def pie_chart():
    songs = load_songs()
    counts = songs["Mood"].value_counts()
    if counts.empty:
        print("No song data available to plot.")
        return
    plt.figure(figsize=(7, 7))
    plt.pie(counts, labels=counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Song Distribution by Mood")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


def bar_graph():
    songs = load_songs()
    # Expected song format: "Song Title by Singer Name"
    singers = songs["Song"].str.extract(r"\s+by\s+(.+)$", flags=0, expand=False)
    counts = singers.dropna().value_counts().head(6)
    if counts.empty:
        print("No singer names found. Use the format 'Song Title by Singer Name'.")
        return
    plt.figure(figsize=(8, 6))
    plt.bar(counts.index, counts.values, edgecolor="black")
    plt.title("Most Frequently Listed Singers")
    plt.xlabel("Singer")
    plt.ylabel("Number of songs")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.show()


def main_menu():
    while True:
        print("\n=== Mood-Based Song Recommender ===")
        print("1. Recommend songs by mood")
        print("2. View mood categories")
        print("3. Add a new user")
        print("4. Exit")
        print("5. Add a new song")
        print("6. Remove a song")
        print("7. Show all songs")
        print("8. Show pie chart")
        print("9. Show singer bar graph")

        choice = input("Choose an option (1-9): ").strip()
        try:
            if choice == "1":
                recommend_songs()
            elif choice == "2":
                view_categories()
            elif choice == "3":
                add_user()
            elif choice == "4":
                print("Thank you for using the Song Recommender!")
                break
            elif choice == "5":
                add_song()
            elif choice == "6":
                remove_song()
            elif choice == "7":
                show_all_songs()
            elif choice == "8":
                pie_chart()
            elif choice == "9":
                bar_graph()
            else:
                print("Invalid choice. Please enter a number from 1 to 9.")
        except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
            print(f"Could not complete that action: {error}")


if __name__ == "__main__":
    if login():
        main_menu()
