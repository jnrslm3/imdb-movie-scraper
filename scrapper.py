import requests
from bs4 import BeautifulSoup


def scrap(ui: list) -> list:
    year, genre, rng = ui
    url = make_url(year, genre)
    return main(url, rng, ui)



def make_url(year: int, genre: str) -> str:
    return f"https://www.imdb.com/search/title/?genres={genre}&year={year},{year}&title_type=feature&sort=user_rating,desc"



def main(url_link: str, rng: int, ui: list = None) -> list:
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url_link, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select(".ipc-metadata-list-summary-item")[:rng]

    if ui:
        year, genre, rng = ui
        print(f"\nMovies based on:\nYear: {year}\nGenre: {genre}\nRange: {rng}\n")

    results = []
    for item in items:
        title = item.select_one("h3").text.strip()

        rating_elem = item.select_one(".ipc-rating-star--rating")
        rating = rating_elem.text.strip() if rating_elem else "N/A"

        print(f"{title} - {rating} ⭐")
        results.append((title, rating))

    print(f"\nFound {len(results)} out of {rng} requested films.\n")
    return results
