import random as rand
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w","--word", help = "Word to seed", type = str)
parser.add_argument("-s","--symmetric", action = "store_true", help = "symmetric")
parser.add_argument("-d","--difficulty", help = "difficulty",type = int)
args = parser.parse_args()

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.EOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def index(self, a: str):
        return ord(a) - ord("a")

    def insert(self, s: str):
        node: TrieNode = self.root
        assert node is not None
        for c in s:
            if node.children[self.index(c)] == None:
                node.children[self.index(c)] = TrieNode() # type: ignore

            node = node.children[self.index(c)] # type: ignore
        
        node.EOW = True # type: ignore

        return True

    def findstart(self, s):
        node = self.root
        assert node is not None
        for i in range(len(s)):
            if node.children[self.index(s[i])]: # type: ignore
                node = node.children[self.index(s[i])] # type: ignore

            else:
                return False

        return True

    def find(self, s):
        node = self.root

        for i in range(len(s)):
            if node.children[self.index(s[i])]: # type: ignore
                node = node.children[self.index(s[i])] # type: ignore

            else:
                return False

        return node.EOW # type: ignore

class Dictionary:
    def __init__(self, word_length, difficulty):
        self.word_length = word_length
        self.difficulty = difficulty

        dictionary = self.dictionary_name(self.word_length)

        self.word_list = []

        with open(dictionary, "r") as text:
            text_file = text.read().splitlines()

            for text_line in text_file:
                if len(self.word_list) >= self.difficulty:
                    break

                if len(text_line) == self.word_length:
                    self.word_list.append(text_line)

        self.trie = Trie()
        self.build_dictionary()

        return

    def dictionary_name(self, num):
        return (
            os.getcwd()
            +"/dictionaries/words_final_"
            + str(num)
            + "_letter.txt"
        )

    def build_dictionary(self):
        for i in self.word_list:
            if len(i) == self.word_length:
                self.trie.insert(i)
        return

class WordSquare:
    def __init__(self, s, symmetric, difficulty):
        print("Word Square Generator")
        self.symmetric = symmetric
        self.word_length = len(s) if s else 5

        self.dictionary = Dictionary(self.word_length, difficulty)
        self.word_list = self.dictionary.word_list
        self.trie = self.dictionary.trie

        self.square = [[None] * self.word_length for i in range(self.word_length)]
        self.squares = 0

        if s == None:
            self.seed = self.word_list[rand.randint(0, len(self.word_list))]
        else:
            self.seed = s.lower()

        for i in range(self.word_length):
            self.square[0][i] = self.seed[i]
            if self.symmetric:
                self.square[i][0] = self.seed[i]

        print(
            "Trying: %s with difficulty %d"
            % (self.seed.upper(), self.dictionary.difficulty)
        )

        self.guess(0)

        print(
            "%d %s Word Square(s) of size %d Found for %s"
            % (
                self.squares,
                "Symmetric" if self.symmetric else "Unsymmetric",
                self.word_length,
                self.seed,
            )
        )

        return

    def printsquare(self):
        for row in range(self.word_length):
            for col in range(self.word_length):
                print(
                    self.square[row][col].upper() if self.square[row][col] else " ",
                    end=" ",
                )

            print()

        print()

        return

    def guess(self, number):
        row = number // self.word_length
        col = number % self.word_length

        if number >= self.word_length * self.word_length:
            self.squares += 1
            self.printsquare()
            return

        if self.square[row][col] != None:
            self.guess(number + 1)
            return

        row_word, col_word = "", ""

        for r in range(row):
            col_word += self.square[r][col]

        for c in range(col):
            row_word += self.square[row][c]

        for alphabet in "abcdefghijklmnopqrstuvwxyz":
            if self.trie.findstart(row_word + alphabet) and self.trie.findstart(
                col_word + alphabet
            ):
                self.square[row][col] = alphabet

                if self.symmetric:
                    self.square[col][row] = alphabet

                self.guess(number + 1)

                self.square[row][col] = None

                if self.symmetric:
                    self.square[col][row] = None

if __name__ == "__main__":
    word = args.word if args.word else input("Word: ")
    symmetric = args.symmetric if args.symmetric else False
    difficulty = args.difficulty if args.difficulty else int(input("Difficulty: "))

    # try_word = WordSquare(word,True,difficulty)

    try_word = WordSquare(word, symmetric, difficulty)
