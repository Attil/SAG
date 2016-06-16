from __future__ import division
from collections import Counter, defaultdict
from math import factorial

from solver import SolverAgent

def binomial_coeff(a, b):
    return factorial(a) / (factorial(a-b) * factorial(b))

class PairAgent(SolverAgent):
    def solve(self, cards):
        if len(cards) > 7:
            return -1  # Error

        cards = [card.split(':')[1] for card in cards]

        if len(cards) != len(set(cards)):
            return 1  # There is already a pair

        got = len(cards)
        left = 7 - got

        bad = (4 ** left) * factorial(13-got) * factorial(52-7)
        bad /= factorial(52-got) * factorial(13-7)

        return 1-bad


class RoyalFlushAgent(SolverAgent):
    def solve(self, cards):
        got = len(cards)

        if got > 7:
            return -1  # Error

        cards = [card.split(':') for card in cards]

        colors = defaultdict(list)
        for card in cards:
            colors[card[0]].append(card[1])

        required = {'a', 'k', 'q', 'j', '10'}

        possible = 0

        for color in colors.values():
            lack = 5-len(required.intersection(color))
            if lack <= 7 - got:
                possible += binomial_coeff(52 - got - lack, 7 - got - lack) * factorial(7 - got - lack)

        return possible / binomial_coeff(52 - got, 7 - got)


if __name__ == '__main__':
    pair = PairAgent("pair@127.0.0.1", "secret")
    pair.start()
    royal_flush = RoyalFlushAgent("royal_flush@127.0.0.1", "secret")
    royal_flush.start()
    try:
    	while True:
    		pass
    except KeyboardInterrupt:
    	pair.stop()
        royal_flush.stop()
