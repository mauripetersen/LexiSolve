from tkinter import messagebox
from enum import StrEnum
import os

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class Language(StrEnum):
    PTBR = "pt-br"
    EN = "en"


def main() -> None:
    while True:
        os.system("cls")
        print("Select the language:\n[0] PT-BR\n[1] EN\n[e] Exit")
        res1 = input("input: ").lower()

        if res1 == "e":
            return
        elif res1 in ["0", "1"]:
            lang: Language = Language.PTBR
            if res1 == "0":
                lang = Language.PTBR
            elif res1 == "1":
                lang = Language.EN
                # print("")
                # print("English language is not yet available.")
                # print("")
                # input("press any key to left...")
                # return

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

            kl_list: list[tuple[str, list[int]]] = []
            fl_list: list[str] = []
            main_loop = True
            while main_loop:
                print("")
                print("Known Letter and Place [klp]")
                klp: str = "a"
                while len(klp) != ws and klp != "":
                    klp = input("klp: ").lower()  # known letter and place
                if klp == "":
                    klp = klp.ljust(ws, "-")

                print("")
                print("Known Letters [kl]")  # known letters
                flag_loop_1 = True
                while flag_loop_1:
                    letter = input("letter: ").lower()

                    if letter == "":
                        flag_loop_1 = False
                    else:
                        if letter in alphabet:
                            fps: list[int] = []  # forbidden places
                            flag_loop_2 = True
                            while flag_loop_2:
                                fp = input("fp: ").lower()  # forbidden place

                                if fp == "":
                                    if any(item[0] == letter for item in kl_list):  # kl_list already have letter
                                        for i, (i_letter, i_fps) in enumerate(kl_list):
                                            if i_letter == letter:
                                                kl_list[i] = (letter, list(set(i_fps) | set(fps)))
                                    else:
                                        kl_list.append((letter, fps))

                                    flag_loop_2 = False
                                else:
                                    if fp.isdigit():
                                        if 1 <= int(fp) <= ws:
                                            fps.append(int(fp))
                                        else:
                                            messagebox.showwarning("ERROR", "fp must satisfy: 1 <= fp <= ws .")
                                    else:
                                        messagebox.showwarning("ERROR", "fp must be an integer.")
                        else:
                            messagebox.showwarning("ERROR", f"'{letter}' doesn't belong to alphabet.")

                print("")
                print("Forbidden Letters [fl]:")  # forbidden letters
                flag_loop = True
                while flag_loop:
                    letter = input("letter: ").lower()

                    if letter == "":
                        flag_loop = False
                    else:
                        if letter in alphabet:
                            if any(item == letter for item in fl_list):
                                messagebox.showwarning("WARNING", f"'{letter}' already in fl_list.")
                            else:
                                fl_list.append(letter)
                        else:
                            messagebox.showwarning("ERROR", f"'{letter}' doesn't belong to alphabet.")

                print("")
                print(f"word size: {ws}")
                print(f"known letters and places: {klp}")
                print(f"known letters: {kl_list}")
                print(f"forbidden letters: {fl_list}")

                res2 = "a"
                while res2 not in ["y", "", "n"]:
                    res2 = input("confirm? [y/n]: ").lower()

                if res2 in ["y", ""]:
                    search_word(lang, ws, klp, kl_list, fl_list)

                print("")
                print("Select an option:\n[c] continue\n[r] restart\n[e] Exit")
                res3 = "a"
                while res3 not in ["c", "", "r", "e"]:
                    res3 = input("option: ").lower()

                if res3 in ["c", ""]:
                    print("")
                    print("continuing...")
                elif res3 in ["r"]:
                    main_loop = False
                elif res3 in ["e"]:
                    return


def search_word(lang: Language, ws: int, klp: str, kl_list: list[tuple[str, list]], fl_list: list[str]) -> None:
    txt_path: str = ""
    if lang == Language.PTBR:
        txt_path = "languages/ptbr.txt"
    elif lang == Language.EN:
        txt_path = "languages/en.txt"
    words = []

    # try:
    if os.path.exists(txt_path) and os.path.isfile(txt_path):
        with open(txt_path, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip().lower()

                if match(word, ws, klp, kl_list, fl_list):
                    words.append(word)

        print("")
        print("")
        print("words found:")
        for w in words:
            print(w)

    #     else:
    #         messagebox.showwarning("ERROR", f"File of {lang} words not found.")
    #         return None
    # except Exception as e:
    #     messagebox.showerror("ERROR", str(e))
    #     return None


def match(word: str, ws: int, klp: str, kl_list: list[tuple[str, list]], fl_list: list[str]) -> bool:
    if len(word) != ws:
        return False
    else:
        # KLP:
        for i in range(ws):
            if klp[i] in alphabet and word[i] != klp[i]:
                return False
            
        # KL:
        for _, (kl, fp) in enumerate(kl_list):
            cont = 0
            for i in range(ws):
                if word[i] == kl:
                    if i + 1 in fp:
                        return False
                    else:
                        cont += 1
            if cont == 0:
                return False

        # FL:
        for fl in fl_list:
            for i in range(ws):
                if klp[i] not in alphabet and word[i] == fl:
                    return False

        return True


if __name__ == "__main__":
    main()
