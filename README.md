🎬 IMDb Movie Scraper

A simple and interactive Python CLI tool that fetches top-rated IMDb movies by year, genre, and range.
Built using requests and BeautifulSoup, this project provides a clean example of web scraping, input validation, and CLI design.

⭐ Features

🔎 Search by criteria

Year (1950 → current year)

Genre (with fuzzy matching suggestions)

Result count (1–25)

⚙️ Robust IMDb scraping

Uses real browser headers

Extracts movie titles and ratings

Handles missing ratings gracefully

🤝 Interactive experience

Guided input prompts

Full validation for all fields

Easy “search again” loop

Clear and readable output formatting

🧹 Clean code structure

main.py
scrapper.py
inputs.py
📦 Installation

Clone the repository:

git clone https://github.com/your-username/imdb-movie-scraper.git
cd imdb-movie-scraper


Install dependencies:

pip install requests beautifulsoup4

🚀 How to Run

Start the program:

python main.py


Follow the CLI prompts:

Enter a year: 2008
Enter a genre (or '?' for help): war
Enter a range (1–25): 10
Are these correct? (y/n): y


Example output:

Movies based on:
Year: 2008
Genre: war
Range: 10

1. The Hurt Locker – 7.6 ⭐
2. Valkyrie – 7.1 ⭐

Found 10 out of 10 requested films.

🗂 Project Structure
📁 imdb-movie-scraper
 ├── main.py            # Application loop and flow control
 ├── scrapper.py        # IMDb scraping logic
 ├── inputs.py          # User input and validation
 ├── README.md
 └── requirements.txt   # Dependencies (optional)

🧪 Technologies Used

Python 3.10+

Requests (HTTP client)

BeautifulSoup4 (HTML parsing)

Difflib (fuzzy matching)

⚠️ Disclaimer

This project is intended for educational and personal use.
Always follow IMDb’s Terms of Service when scraping.
