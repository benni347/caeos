#!/usr/bin/env python
"""
This is my interpreter
:Author: benni347@github.com
"""
import random as rnd
import re  # for regex
import math

lst = []


class Main:
    def __init__(self):
        self.code: str = ""

    def set_code(self, code):
        """
        Sets the code to be used in the program.
        :param code: a str
        :return: None
        """
        self.code = code

    def get_code(self):
        """
        Returns the code.
        :return: a str
        """
        return self.code

    def ask_user(self):
        """
        Ask the user if he wants to writer the code in the terminal or to load from a file
        :return:
        """
        print("Do you want to write the code in the terminal or load from a file?")
        print("1. Write in the terminal")
        print("2. Load from a file")
        choice = input("Choice: ")
        if choice == "1":
            self.write_code()
        elif choice == "2":
            self.load_code()
        else:
            print("Invalid choice")
            self.ask_user()

    def write_code(self):
        """
        Write the code in the terminal.
        :return: None
        """
        print("Write the code in the terminal")
        self.code = input("Code: ")
        sequence = self.find_sequence(self.get_code())
        self._print(sequence)

    def load_code(self):
        """
        Load the code from a file.
        :return: None
        """
        print("Load the code from a file")
        file_name = input("File name: ")
        try:
            with open(file_name, "r") as f:
                self.code = f.read()
                sequence = self.find_sequence(self.get_code())
                self._print(sequence)
        except FileNotFoundError:
            print("File not found")
            self.load_code()

    @staticmethod
    def find_sequence(inp: str) -> list:
        """
        Finds the sequence in the code.
        :param inp: a str
        :return: a list of the sting
        """
        return re.findall(r"\{+.*?}}", inp)

    @staticmethod
    def _print(inp):
        global lst
        for l in inp:
            l = l.replace("{", "").replace("}", "")
            for i in l:
                b = ord(i) + rnd.randrange(ord(i), ord(i) * ord(i))
                while b > 126:
                    b = math.sqrt(b)

                omp = chr(round(b))
                lst.append(omp)
            print("".join(lst))
            lst = []  # empty the list for next input


if __name__ == "__main__":
    main = Main()
    main.ask_user()
