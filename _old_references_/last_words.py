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

            res2 = ""
            print("")
            while not res2.isdigit():
                res2 = input("s1: ").lower()
            s1: int = int(res2)

            res2 = ""
            while not res2.isdigit():
                res2 = input("s2: ").lower()
            s2: int = int(res2)
            print("")

            last_words: list[tuple[int, int, str]] = []
            txt_path = "languages/ptbr.txt"
            with open(txt_path, "r", encoding="utf-8") as f:
                for size in range(s1, s2 + 1):
                    last_k = 0
                    last_letter = "a"

                    for k, letter in enumerate(alphabet):
                        f.seek(0)
                        flag_found_one = False
                        for line in f:
                            word = line.strip().lower()

                            if len(word) == size and not any(alphabet[x] in word for x in range(0, k + 1)):
                                flag_found_one = True
                                break

                        if flag_found_one:
                            last_k = k
                            last_letter = letter
                        else:
                            last_words.append((size, last_k, last_letter))
                            break

            for (a, b, c) in last_words:
                print(f"{a}\t{b}\t{c}")
            print("")
            input("press any key to left...")


if __name__ == "__main__":
    main()
