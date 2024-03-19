import sys

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand:
    def __init__(self, hand):
        self.hand = hand
        self.category = 0
        self.rank = 0
        self.hand.sort(key=lambda x: x.value)
        self.straightFlush()
        self.fourOfAKind()
        self.fullHouse()
        self.flush()
        self.straight()
        self.threeOfAKind()
        self.twoPairs()
        self.pair()
        self.highCard()

    def highCard(self):
        if self.category != 0:
            return
        self.category = 1
        for card in reversed(self.hand):
            self.rank = self.rank * 100 + card.value

    def pair(self):
        if self.category != 0:
            return
        count = self.groups()
        pairs = [c for c, freq in count.items() if freq == 2]
        if len(pairs) == 1:
            self.category = 2
            self.rank = pairs[0]
            for card in reversed(self.hand):
                if card.value != pairs[0]:
                    self.rank = self.rank * 100 + card.value

    def twoPairs(self):
        if self.category != 0:
            return
        count = self.groups()
        pairs = [c for c, freq in count.items() if freq == 2]
        singleton = 0
        for c, freq in count.items():
            if freq == 1:
                singleton = c
        if len(pairs) == 2:
            self.category = 3
            pairs.sort()
            for pair in reversed(pairs):
                self.rank = self.rank * 100 + pair
            self.rank = self.rank * 100 + singleton

    def threeOfAKind(self):
        if self.category != 0:
            return
        count = self.groups()
        for c, freq in count.items():
            if freq == 3:
                self.category = 4
                self.rank = c
                for card in reversed(self.hand):
                    if card.value != c:
                        self.rank = self.rank * 100 + card.value
                return

    def straight(self):
        if self.category != 0:
            return
        value = self.hand[0].value
        for card in self.hand[1:]:
            if card.value - value == 1:
                value = card.value
            else:
                return
        self.category = 5
        self.rank = self.hand[-1].value

    def flush(self):
        if self.category != 0:
            return
        suit = self.hand[0].suit
        for card in self.hand[1:]:
            if card.suit != suit:
                return
        self.category = 6
        for card in reversed(self.hand):
            self.rank = self.rank * 100 + card.value

    def fourOfAKind(self):
        self.fourOfAKindFullHouse(4, 8)

    def fullHouse(self):
        self.fourOfAKindFullHouse(3, 7)

    def fourOfAKindFullHouse(self, n, cat):
        if self.category != 0:
            return
        count = self.groups()
        if len(count) != 2:
            return
        keys = list(count.keys())
        if count[keys[0]] == n:
            self.category = cat
            self.rank = keys[0]
        elif count[keys[1]] == n:
            self.category = cat
            self.rank = keys[1]

    def straightFlush(self):
        if self.category != 0:
            return
        suit = self.hand[0].suit
        value = self.hand[0].value
        for card in self.hand[1:]:
            if card.suit == suit and card.value - value == 1:
                value = card.value
            else:
                return
        self.category = 9
        self.rank = self.hand[-1].value

    def groups(self):
        count = {}
        for card in self.hand:
            count.setdefault(card.value, 0)
            count[card.value] += 1
        return count

def compare(black, white):
    compareCategory = black.category - white.category
    if compareCategory == 0:
        return black.rank - white.rank
    return compareCategory

def getHand(h):
    return Hand([Card(x[0], x[1]) for x in h])

while True:
    currentLine = sys.stdin.readline().strip()
    if not currentLine:
        break
    cmp = compare(getHand(currentLine.split()[:5]), getHand(currentLine.split()[5:]))
    if cmp == 0:
        print("Tie.")