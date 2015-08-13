import poker

def test_message(test_name,hand,board):
	print test_name
	print "hand : ", hand
	print "board : ", board

if __name__=="__main__":
	hm =poker.HM("Waki_G")
	test_name = "high card test"
	hand = ["2d","7d"]
	board = ["3s","4h","5c","8d","9d"]
	test_message(test_name,hand,board)
	print hm.find_hand_role(hand,board)
	
	print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

	test_name = "one pair"
	hand = ["2s","3s"]
	board = ["4c","5c","2d","Td","Kh"]
	test_message(test_name,hand,board)
	print hm.find_hand_role(hand,board)

	print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

	test_name = "two pair"
	hand = ["2d","2s"]
	board = ["3s","5d","3d","Ts","Qh"]
	test_message(test_name,hand,board)
	print hm.find_hand_role(hand,board)

	print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

	test_name = "three of a kind"
	hand = ["2d","2s"]
	board = ["2h","5d","7s","9d","Jh"]
	test_message(test_name,hand,board)
	print hm.find_hand_role(hand,board)

	print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

	test_name = "straight"
	hand = ["3d","4s"]
	board = ["6s","8d","7h","2s","5d"]
	test_message(test_name,hand,board)
	print hm.find_hand_role(hand,board)

	print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

	test_name = "flush"
	hand = ["3d","4d"]
	board = ["2d","5d","Kd","Qh","Jd"]
	test_message(test_name,hand,board)
	print hm.find_hand_role(hand,board)

	print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"



