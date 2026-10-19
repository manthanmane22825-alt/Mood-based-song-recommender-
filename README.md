# Mood-Based Song Recommender 🎵

A beginner-friendly Python project that recommends songs based on the user's mood. It also includes basic user login, song and mood management, and charts for exploring the song dataset.

## Features

- **Login system** using a CSV file of usernames and passwords
- **Mood-based recommendations** for moods such as happy, sad, calm, energetic, romantic, and road trip
- **View mood categories** available in the song dataset
- **Add users** and register new songs
- **Remove songs** from the dataset
- **View all songs** in a formatted table
- **Visualize mood distribution** with a pie chart
- **Visualize singer counts** with a bar chart

## Built With

- Python
- pandas — CSV data handling
- Matplotlib — charts and visualizations
- tabulate — formatted terminal tables

## Project Structure

```text
mood-based-song-recommender/
├── main.py
├── songs.csv
├── users.example.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer recommended
- pip

## Setup and Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/mood-based-song-recommender.git
cd mood-based-song-recommender
```

### 2. Create a virtual environment (recommended)

Windows:

```bash
py -m venv .venv
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the CSV files

Copy `users.example.csv` to `users.csv` in the project folder. The example file contains a demo account:

```csv
Username,Password
demo,demo123
```

This is only a learning example. Do not use a real or reused password.

Create `songs.csv` with these headers:

```csv
Mood,Song
happy,Example Song by Example Singer
sad,Another Example Song by Example Singer
calm,Relaxing Example Song by Example Singer
energetic,Upbeat Example Song by Example Singer
romantic,Romantic Example Song by Example Singer
roadtrip,Road Trip Example Song by Example Singer
```

Replace the examples with songs you are allowed to use. Keep the `Mood,Song` column names so they match the program.

### 5. Run the program

```bash
python main.py
```

Sign in using a row from your local `users.csv` file.

## Menu Options

When you sign in, the program offers options to:

1. Recommend songs based on mood
2. View available mood categories
3. Add a user
4. Exit
5. Add a song
6. Remove a song
7. Display all songs in a table
8. Show a pie chart of mood distribution
9. Show a bar chart of singer counts

## Concepts Practised

- Functions and modular program structure
- User input and conditional statements
- Loops
- CSV file reading and writing
- Data filtering with pandas
- Basic authentication logic
- Data visualization with Matplotlib
- Terminal formatting with tabulate

## Current Limitations / Future Improvements

This is a learning project, not a production-ready authentication system. The demo login stores plain-text passwords in a local CSV file. Before using it beyond practice, consider:

- Use relative paths or `pathlib` so the project works on different computers.
- Never commit real usernames, passwords, or personal data. Keep a `users.example.csv` template instead of real account data.
- Store passwords securely using a suitable password-hashing approach.
- Validate user input and handle missing or malformed CSV files.
- The current `main.py` uses paths relative to the project folder so it can run on different computers.
- Add automated tests and improve error handling.
- The singer chart assumes song names contain text like `Song Title by Singer Name`; adjust the dataset or parsing logic if they do not.
- The chart labels should describe the data accurately; the current chart title says “This Week” although the code counts rows in the CSV and does not track listening dates.

## Disclaimer

This project is for learning and demonstration purposes. It does not stream or play music; it recommends song names from a local CSV dataset.

## Author

**Your Name** — replace this with your name or GitHub profile.

## License

If you want others to reuse the code, add a license such as the MIT License after reviewing its terms. Do not add a license unless you intend to grant those permissions.
