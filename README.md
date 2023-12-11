# Word Square Generator.
- Program to generate symmetric and non-symmetric word squares

## Word Squares:
- A word square is a matrix of nxn size, containing n-letter words.
- An unsymmetric word square is a square such that all the n-length words formed from the letters in each row and each column are valid words.
  Example of a 5x5 unsymmetric word square:
  S | T | A | R | S
  --- | --- | --- | --- | --- 
  **H** | **A** | **B** | **I** | **T**
  **A** | **L** | **O** | **N** | **E**
  **V** | **E** | **R** | **S** | **E**
  **E** | **S** | **T** | **E** | **R**
- A symmetric word square is a square such that the words formed from a row and from the corresponding column are the same.
- Example of a 5x5 symmetric word square:
  V | E | N | U | S
  --- | --- | --- | --- | --- 
  **E** | **X** | **I** | **S** | **T**
  **N** | **I** | **C** | **H** | **E**
  **U** | **S** | **H** | **E** | **R**
  **S** | **T** | **E** | **R** | **N**
## Functionality:
- The program has the options to:
  1. Select a starting word to use as the first row, or use a random word (by setting the word as an empty string).
  2. Select between a symmetric or an unsymmetric Word Square.
  3. Choose a difficulty level based on how commonplace the words can be (A higher difficulty might have words that don't look valid and generate too many squares, while a lower difficulty might not generate a square at all.)

## User Guide:
  1. Clone this repository, with the dictionaries. 
  2. Set the difficulty, initial word and the boolean for symmetric, and run.

## Acknowledgements:
  1. The dictionary has is from multiple dictionaries all over the internet (sgb-words.txt,etc), and has been parsed into different word length dictionaries using Python file ops

## To-Do:
  1. Make faster - Develop on C++, and use words as state space instead of letters 
  2. Make User Interface better
  3. Improve Readme file, add proper acknowledgements
  4. Unsymmetric generates symmetric too, change that 

Thanks for reading this far! Contact me at 4dnaanm@gmail.com for any inquiries :)
