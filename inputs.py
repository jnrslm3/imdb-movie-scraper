from datetime import datetime
from difflib import get_close_matches
import sys

validation = []


def user_input() -> list:
    while True:   
        year = user_date()
        genre = user_genre()
        rng = user_range()

        print("\nYour choices:")
        print(f"Year:  {year}")
        print(f"Genre: {genre}")
        print(f"Range: {rng}")

        choice = input("\nAre these correct? (y/n): ").lower()  
        if choice in ("y", "yes"):
            return [year, genre, rng]  

        print("\nOkay, let's try again!\n") 



def user_date() -> int:
    while True:
        try:
            ui_year = int(input("Enter a year: "))
            current_year = datetime.now().year

            if ui_year < 1950 or ui_year > current_year:
                print(f"Invalid date. Choose between 1950 - {current_year}")
            else:
                return ui_year

        except ValueError:
            print(f"Please enter a year between 1950 - {datetime.now().year}")



def user_genre() -> str:
    genres = [
        "drama", "adventure", "thriller", "crime", "action",
        "mystery", "war", "fantasy", "sci-fi"
    ]

    while True:
        ui_genre = input("Enter a genre (or '?' for help): ").lower()

        if ui_genre in genres:
            return ui_genre

        if ui_genre == "?":
            print("Available genres:", ", ".join(genres))
            continue

        matches = get_close_matches(ui_genre, genres, n=1, cutoff=0.6)
        if matches:
            print(f"Did you mean '{matches[0]}'?")
        else:
            print("Invalid genre. Type '?' to see available genres.")


            
def user_range() -> int:
    while True:
        try:
            ui_range = int(input("Enter a range (1–25): "))           

            if 1 <= ui_range <= 25:
                return ui_range

            print("Please enter a number between 1 and 25.")

        except ValueError:
            print("Only numbers are allowed. Try again.")




