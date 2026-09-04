from tkinter import messagebox
from enum import StrEnum
import os

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class Language(StrEnum):
    PTBR = "pt-br"
    ENG = "eng"


def main() -> None:
    while True:
        os.system("cls")
        print("Select the language:\n[0] PT-BR\n[1] ENG\n[e] Exit")
        res1 = input("input: ").lower()

        if res1 == "e":
            return
        elif res1 in ["0", "1"]:
            lang: Language = Language.PTBR
            if res1 == "0":
                lang = Language.PTBR
            elif res1 == "1":
                lang = Language.ENG
                print("")
                print("English language is not yet available.")
                print("")
                input("press any key to left...")
                return

            print("")
            while True:
                letters = input("letters: ").lower()

                if letters != "":
                    if all(letter in alphabet for letter in letters):
                        break
                    else:
                        messagebox.showwarning("ERROR", f"'{letters}' doesn't belong to alphabet.")

            found = search_anagram(lang, letters)

            print("")
            if len(found) > 0:
                print(f'anagrams of "{letters}":')
                for word in found:
                    print(word)
            else:
                print(f'no anagrams of "{letters}" was found.')

            print("")
            input("press any key to restart...")


def search_anagram(lang: Language, letters: str) -> list[str]:
    txt_path: str = ""
    if lang == Language.PTBR:
        txt_path = "languages/ptbr.txt"
    elif lang == Language.ENG:
        ...
    found = []

    try:
        if os.path.exists(txt_path) and os.path.isfile(txt_path):
            with open(txt_path, "r", encoding="utf-8") as f:
                for line in f:
                    word = line.strip().lower()

                    if match(word, letters):
                        found.append(word)
            return found
        else:
            messagebox.showwarning("ERROR", f"File of {lang} words not found.")
            return []
    except Exception as e:
        messagebox.showerror("ERROR", str(e))
        return []


def match(word: str, letters: str, consider_same: bool = False) -> bool:
    if len(word) == len(letters):
        if all(letters.count(letter) == word.count(letter) for letter in letters):
            if word != letters or consider_same:
                return True
    return False


if __name__ == "__main__":
    main()
