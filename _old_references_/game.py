from tkinter import messagebox
import random
import os

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def main() -> None:
    while True:
        os.system("cls")
        print("Select the language:\n[0] PT-BR\n[e] Exit")
        res1 = input("input: ").lower()

        if res1 == "e":
            return

        if res1 in ["0"]:
            print("")
            while True:
                res2: str = input("word size: ")  # word size
                if res2.isdigit():
                    if int(res2) > 0:
                        break
                    else:
                        messagebox.showwarning("ERROR", "word size must be greater than zero.")
                else:
                    messagebox.showwarning("ERROR", "word size must be an integer.")
            ws: int = int(res2)

            if res1 == "0":
                ptbr(ws)
                print("")
                input("press any key to left...")


def ptbr(ws: int) -> None:
    txt_path = "languages/ptbr.txt"
    words = []

    try:
        if os.path.exists(txt_path) and os.path.isfile(txt_path):
            with open(txt_path, "r", encoding="utf-8") as f:
                for line in f:
                    word = line.strip().lower()

                    if len(word) == ws:
                        words.append(word)
            word = random.choice(words)

            print("")
            print("START")
            while True:
                attempt = input().lower()

                if len(attempt) == len(word):
                    if all(x in alphabet for x in attempt):
                        if attempt == word:
                            print("".ljust(ws,"2"))
                            print("")
                            print("well done!")
                            return

                        print(match(word, attempt))
                        print("")

        else:
            messagebox.showwarning("ERROR", f"File of pt-br words not found.")
            return None
    except Exception as e:
        messagebox.showerror("ERROR", str(e))
        return None


def match(word: str, attempt: str) -> str:
    code: str = ""
    for i in range(0, len(word)):
        if attempt[i] == word[i]:
            code += "2"
        else:
            cont = 0
            for k in range(0, len(word)):
                if attempt[i] == word[k]:
                    cont += 1
            if cont == 0:
                code += "0"
            else:
                code += "1"
    return code


if __name__ == "__main__":
    main()

    print("")
    print("Done.")
