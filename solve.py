#!/usr/bin/python3
from nyt_wordle_list import it as words

def contains_all(l,s):
  for i in l:
    if i not in s:
      return False
  return True 

def contains_none(l,s):
  for i in l:
    if i in s:
      return False
  return True 

import string 

contains_dic = {}
not_contains_dic = {}

all_words = set(words)

for letter in string.ascii_lowercase:
  contains_dic[letter] = set([w for w in words if letter in w])
  not_contains_dic[letter] = all_words.difference(contains_dic[letter])

def num_candidates(guess,word,wordlist=all_words):
  guess_set = set(guess)
  word_set = set(word)
  same_letters = guess_set.intersection(word_set)
  not_same_letters = guess_set.difference(word_set)
  cands = wordlist
  #words with and without letters
  for letter in same_letters:
    cands = cands.intersection(contains_dic[letter])
  for letter in not_same_letters:
    cands = cands.intersection(not_contains_dic[letter])
  #correct letter locations
  for letter in same_letters:
    for i in range(5):
      if guess[i] == letter:
        #right letter right place
        if word[i] == letter:
          cands2 = set()
          for w in cands:
            if w[i] != letter:
              cands2.add(w)
          cands = cands.difference(cands2)
        #right letter wrong place
        if word[i]!=letter:
          cands2 = set()
          for w in cands:
            if w[i]==letter:
              cands2.add(w)
          cands = cands.difference(cands2)


  return cands

def find_best_guess(cands):
  best_cands = len(cands)
  best_word = None
  for guess in words:
    worst_case = 0
    for word in cands:
      cands2 = num_candidates(guess,word,wordlist=cands)
      if len(cands2) > worst_case:
        worst_case = len(cands2)
    if worst_case < best_cands:
      best_cands = worst_case 
      best_word = guess
    
  return best_cands,best_word

def find_best_guess2(cands):
  best_cands = len(cands)
  best_word = None
  worst_cases = []
  guesses = []
  for guess in words:
    worst_case = 0
    for word in cands:
      cands2 = num_candidates(guess,word,wordlist=cands)
      if len(cands2) > worst_case:
        worst_case = len(cands2)
    if worst_case < best_cands:
      best_cands = worst_case 
      best_word = guess
    
    worst_cases.append(worst_case)
    guesses.append(guess)
  return worst_cases,guesses


import argparse

parser = argparse.ArgumentParser(
                    prog = 'Wordle Solver',
                    description = 'A program for cheating at wordle',
                    )

# parser.add_argument('n1', nargs='*',
#                     help='an integer for the accumulator')
# parser.add_argument('--n1', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                  help='Yellow letters for position 1.')

# parser.add_argument('n2',  nargs='*',
#                     help='an integer for the accumulator')
# parser.add_argument('--n2', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                  help='Yellow letters for position 2.')

# parser.add_argument('n3',  nargs='*',
#                     help='an integer for the accumulator')
# parser.add_argument('--n3', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                  help='Yellow letters for position 3.')

# parser.add_argument('n4',  nargs='*',
#                     help='an integer for the accumulator')
# parser.add_argument('--n4', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                  help='Yellow letters for position 4.')

# parser.add_argument('n5',  nargs='*',
#                     help='an integer for the accumulator')
# parser.add_argument('--n5', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                  help='Yellow letters for position 5.')


parser.add_argument('--y1', nargs='*',type=str,
                    help='an integer for the accumulator')


parser.add_argument('--y2', nargs='*',
                    help='an integer for the accumulator')

parser.add_argument('--y3', nargs='*',
                    help='an integer for the accumulator')

parser.add_argument('--y4', nargs='*',
                    help='an integer for the accumulator')

parser.add_argument('--y5', nargs='*',
                    help='an integer for the accumulator')

parser.add_argument('--g1', 
                    help='an integer for the accumulator')
parser.add_argument('--g2', 
                    help='an integer for the accumulator')
parser.add_argument('--g3', 
                    help='an integer for the accumulator')
parser.add_argument('--g4', 
                    help='an integer for the accumulator')
parser.add_argument('--g5', 
                    help='an integer for the accumulator')

parser.add_argument('--bad', 
                    help='an integer for the accumulator')

parser.add_argument('-l', action='store_true',
                    help='Flag to list possible solutions')

parser.add_argument('-g', action='store_true',
                    help='Calculate best next move')

args = parser.parse_args()
# print(args)

def args_to_func(args):
    def foo(w):
        if args.bad!=None:
            if not contains_none(args.bad,w):
                return False
        #yellow letters
        if args.y1!=None:
            for c in args.y1:
                if c not in w:
                    return False
                if w[0]==c:
                    return False

        if args.y2!=None:
            for c in args.y2:
                if c not in w:
                    return False
                if w[1]==c:
                    return False
        if args.y3!=None:
            for c in args.y3:
                if c not in w:
                    return False
                if w[2]==c:
                    return False
        if args.y4!=None:
            for c in args.y4:
                if c not in w:
                    return False
                if w[3]==c:
                    return False
        if args.y5!=None:
            for c in args.y5:
                if c not in w:
                    return False
                if w[4]==c:
                    return False
        
        #green letters
        if args.g1!=None:
            if args.g1!=w[0]:
                return False
        if args.g2!=None:
            if args.g2!=w[1]:
                return False
        if args.g3!=None:
            if args.g3!=w[2]:
                return False
        if args.g4!=None:
            if args.g4!=w[3]:
                return False
        if args.g5!=None:
            if args.g5!=w[4]:
                return False
        return True
    
    return foo 

func = args_to_func(args)

cands = [w for w in words if func(w)]

if args.l:
    for c in cands[:200]:
        print(c)
    print(len(cands),' possibilities')

if args.g:
    x,y = find_best_guess2(set(cands))
    s = list(set(x))
    for i in range(4):
        print('worst case',s[i])
        guesses = [word for worst_case,word in zip(x,y) if worst_case==s[i] ]
        if len(guesses) > 50:
            print(guesses[:50])
        else:
            print('guesses',guesses)
    


    