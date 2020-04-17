#!/c/Users/Bryan/AppData/Local/Programs/Python/Python38/python

import sys


def rock_paper_scissors(n):
    base = [['rock'], ['paper'], ['scissors']]
    possibleResults = [0] * 3 ** n
    print(possibleResults)
    if n == 0:
        return [[]]
    if n == 1:
        return base
    recursion = rock_paper_scissors(n-1)
    i = 0
    for item in recursion:
        for action in base:
            possibleResults[i] = item + action
            i += 1
    return possibleResults

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')