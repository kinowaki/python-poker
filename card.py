#-*-coding:utf-8-*-

import random

class Card:
	amount = 52
	def __init__(self):
		self.card_nums = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q","K","A"]
		self.card_kinds = ["s", "c", "d", "h"]
		self.deck = []
		for num in self.card_nums:
			for kind in self.card_kinds:
				self.deck.append(str(num)+kind)

	def shuffle(self):
		random.shuffle(self.deck)

	def push(self):
		#number + kind :2d, As 
		return self.deck.pop()
'''
if  __name__=="__main__":
	card = Card()
	print card.deck, len(card.deck)
	card.shuffle()
	print card.deck, len(card.deck)
	print card.push(), len(card.deck)
'''
