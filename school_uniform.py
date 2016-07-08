card_order = ["0","3","4","5","6","7","8","9","10","J","Q","K","A","2"]

given_cards = raw_input().split()
rank = [0 for i in range(0, len(given_cards))]

while given_cards.count("0") < 52:
    #print(given_cards)
    for rank, card in given_cards:
        if card_order.index(card) > card_order.index(field):
            field = given_cards[idx]
            given_cards[idx] = "0"
            #print str(rank) + ": ",
            print("idx: " + str(idx) + " card: " + str(card) + " field: " + str(field))
            #print(str(idx + 1))
    else:
        field = "0"

def rebuild_list(list=[], split_index):
    tmp = list[0:split_index]

