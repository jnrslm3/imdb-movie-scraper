from inputs import user_input
from scrapper import scrap
import sys

def continue_prompt() -> bool:
    while True:
        ui = input("Enter 'exit'/'e' to quit or 'movie'/'m' to search again: ").strip().lower()

        if ui in ("exit", "e"):
            return False
        if ui in ("movie", "m"):
            print()
            return True

        print("Invalid input.")
            

def run():
    while True:
        scrap(user_input())

        if not continue_prompt():
            print("Good bye.")
            sys.exit()

if __name__ == "__main__":
    run()