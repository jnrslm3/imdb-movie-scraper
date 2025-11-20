🎬 IMDb Movie Scraper

IMDb Movie Scraper is a Python CLI tool that retrieves top-rated movies from IMDb based on year, genre, and range. Built with requests and BeautifulSoup, it provides a reliable and interactive command-line experience.

🚀 Features

🔹 Fetch movies by year, genre, and range (1–25)

🔹 Interactive CLI with input validation and confirmation

🔹 Displays movie titles and IMDb ratings

🔹 Handles missing ratings gracefully

🔹 Clean and modular Python code structure (main.py, scrapper.py, inputs.py)

🛠 Technologies

Python 3.10+

Requests — HTTP client

BeautifulSoup4 — HTML parser

Difflib — fuzzy genre matching

📦 Installation
git clone https://github.com/your-username/imdb-movie-scraper.git
cd imdb-movie-scraper
pip install requests beautifulsoup4

🎮 Usage

Run the program:

python main.py


Follow the prompts:

Enter a year: 2014
Enter a genre (or '?' for help): sci-fi
Enter a range (1–25): 10
Are these correct? (y/n): y


Example output:

Movies based on:
Year: 2014
Genre: sci-fi
Range: 10

1. Interstellar – 8.7 ⭐
2. Edge of Tomorrow – 7.9 ⭐
...

Found 10 out of 10 requested films.

⚠️ Disclaimer

This project is for educational and personal use only.
Always comply with IMDb’s Terms of Service when scraping.
