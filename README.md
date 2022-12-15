# wordle-bot
A python script that can always solve the nyt wordle game

Usage
`
usage: Wordle Solver [-h] [--y1 [Y1 [Y1 ...]]] [--y2 [Y2 [Y2 ...]]]
                     [--y3 [Y3 [Y3 ...]]] [--y4 [Y4 [Y4 ...]]]
                     [--y5 [Y5 [Y5 ...]]] [--g1 G1] [--g2 G2] [--g3 G3]
                     [--g4 G4] [--g5 G5] [--bad BAD] [-l] [-g]

A program for cheating at wordle

optional arguments:
  -h, --help          show this help message and exit
  --y1 [Y1 [Y1 ...]]  list of yellow letters in the 1st column
  --y2 [Y2 [Y2 ...]]  list of yellow letters in the 2nd column
  --y3 [Y3 [Y3 ...]]  list of yellow letters in the 3rd column
  --y4 [Y4 [Y4 ...]]  list of yellow letters in the 4th column
  --y5 [Y5 [Y5 ...]]  list of yellow letters in the 5th column
  --g1 G1             green letter in the 1st column
  --g2 G2             green letter in the 2nd column
  --g3 G3             green letter in the 3rd column
  --g4 G4             green letter in the 4th column
  --g5 G5             green letter in the 5th column
  --bad BAD           string of letters not contained in the word
  -l                  Flag to list possible solutions
  -g                  Calculate best next move
`
