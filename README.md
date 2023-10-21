# Word Square Generator.
- Program to generate symmetric and non-symmetric word squares

## Word Squares:
- A word square is a matrix of nxn size, containing n-letter words.
- An unsymmetric word square is a square such that all the n-length words formed from the letters in each row and each column are valid words.
- A symmetric word square is a square such that the words formed from a row and from the corresponding column are the same.

## Functionality:
- The program has the options to:
  1. Select a starting word to use as the first row, or use a random word (by setting the word as an empty string).
  2. Select between a symmetric or an unsymmetric Word Square.
  3. Choose a difficulty level based on how commonplace the words can be (A higher difficulty might have words that don't look valid and generate too many squares, while a lower difficulty might not generate a square at all.)

## User Guide:
  1. Clone this repository, with the dictionaries. 
  2. Change the part of the "stringmaker" method that says '/Users/Adnaan/Downloads/Diro_Behavior/Code/Word Square' to the path that your repository is on
  3. Set the difficulty, initial word and the boolean for symmetric, and run on terminal.

## Acknowledgements:
  1. The dictionary has is from multiple dictionaries all over the internet (sgb-words.txt,etc), and has been parsed into different word length dictionaries using Pandas

## To-Do:
  1. Make faster - Develop on C++, and use words as state space instead of letters 
  2. Make User Interface better
  3. Improve Readme file, add proper acknowledgements

Thanks for reading this far! Contact me at 4dnaanm@gmail.com for any inquiries :)
