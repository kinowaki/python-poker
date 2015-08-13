#-*-coding:utf-8-*-
import card

class HM:
	def __init__(self,player_num):
		self.player_num = player_num
	
	"""find hand role"""
	def find_hand_role(self,player_card,boad_card):
		mixed_cards = player_card + boad_card
		is_straight,num_cards = self.straight_check(mixed_cards)
		pair_dict = self.pair_check(mixed_cards)
		pair_keys = pair_dict.keys()
		pair_values = pair_dict.values()
		is_flush,which_kind,flush_cards = self.flush_check(mixed_cards)
		if is_flush and is_straight:
			return "straight flush", flush_cards
		elif max(pair_values) == 4:
			keys = pair_dict.keys()
			num4 = 0
			for key in keys:
				val = pair_dict[key]
				if val == 4:
					num = val
			return "four of a kind",num
		elif max(pair_values) == 3 and 2 in pair_values:
			return "full house"
		elif is_flush and not is_straight:
			return "flush", flush_cards
		elif not is_flush and is_straight:
			return "straight",num_cards
		elif max(pair_values) == 3 and 2 not in pair_values:
			return "three of kind"
		elif pair_values.count(2) >= 2:
			return "two pair"
		elif pair_values.count(2) == 1:
			return "one pair"
		else:
			return "high card",num_cards
	
	def cards_separate(self,mixed_cards,which):
		cards = []
		for card in mixed_cards:
			cards.append(card[which])
		return cards
	
	def cards_translate(self,num_cards):
		if "A" in num_cards:
			num_cards.remove("A")
			num_cards.append(1)
			num_cards.append(14)
		tag_trans = ["T","J","Q","K"]
		ref_trans = {"T":10,"J":11,"Q":12,"K":13}
		for tag in tag_trans:
			if tag in num_cards:
				num_cards.remove(tag)
				num_cards.append(ref_trans[tag])
		return num_cards

	def num_separate(self,mixed_cards):
		return self.cards_separate(mixed_cards,which=0)
	
	def kind_separate(self,mixed_cards):
		return self.cards_separate(mixed_cards,which=1)

	def pair_check(self,mixed_cards):
		num_cards = self.num_separate(mixed_cards)
		num_uniq_keys = list(set(num_cards))
		pair_dict = {}
		for num in num_uniq_keys:
			amount = num_cards.count(num)
			pair_dict[num] = amount		
		return pair_dict

	def straight_check(self,mixed_cards):
		num_cards = self.num_separate(mixed_cards)
		num_cards_trans = self.cards_translate(num_cards)
		num_uniq_keys = list(set(num_cards_trans))
		num_high_straight = []
		num_high_cards = []
		if len(num_uniq_keys) >=5:
			for num in num_uniq_keys:
				num_straight = range(int(num),int(num)+5)
				num_compare = set(num_straight).intersection(set(num_uniq_keys))
				if len(num_compare) == 5:
					num_high_straight = num_straight
			if len(num_high_straight) == 0:
				key_len = len(num_uniq_keys)
				if key_len > 5:
					num_high_card = num_uniq_keys[key_len-5:key_len]
				else:
					num_high_card = num_uniq_keys
				return False,num_high_card
			else:
				print "a"
				return True,num_highstraight
		else:
			return False,num_high_card
	def flush_check(self,mixed_cards):
		kind_cards = self.kind_separate(mixed_cards)
		kind_keys = ["s","c","d","h"]
		kind_dict = {}
		for key in kind_keys:
			kind_dict[key] = self.kind_count(kind_cards,key)
		is_flush = False
		which_kind = ""
		flush_cards = []
		for key in kind_keys:
			if kind_dict[key]>=5:
				is_flush = True
				which_kind = key
				kind_index = kind_cards.index(key)
				print kind_index
				for n in kind_index:
					flush_cards.append(mixed_card[n])	
		return is_flush,which_kind,flush_cards
	
	def kind_count(self,kind_cards,kind_key):
		count = kind_cards.count(kind_key)
		return count

	"""end find hand role"""

