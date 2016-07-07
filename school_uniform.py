card_order = ["0","3","4","5","6","7","8","9","10","J","Q","K","A","2"]

given_cards = raw_input().split()
field = "0"
rank = 0

while len(given_cards):
    print(given_cards)
    tmp_list = given_cards
    for idx, card in enumerate(tmp_list):
        if card_order.index(card) > card_order.index(field):
            field = given_cards.pop(idx)
            rank += 1
            print str(rank) + ": ",
            print("dbg: " + str(card) + " " + str(idx) + " " + str(field))
    
