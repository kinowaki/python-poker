# -*- coding: utf-8 -*-

class Player:
	
	def __init__(self, name=None):
		self.name = name

	def get_info(self,info):
		self.position = info.position
		self.last_bet_amount = info.last_bet_amount
		self.min_bet = info.min_bet

	def action(self):
		while True:
			print "0:fold, 1;call, 2:raise"
			self.act = input()
			if self.act < 0 or self.act > 3:
				print "invalid input"
			else:
				return self.act

	def bet(self):
		self.bet_amount = input()

if __name__=="__main__":
	player1 = Player("Waki_G")
	player2 = Player()
	print player1.action()

		
