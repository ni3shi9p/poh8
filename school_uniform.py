card_order = ["0","3","4","5","6","7","8","9","10","J","Q","K","A","2"]

given_cards = raw_input().split()
rank_list = [0 for i in range(0,len(given_cards))]
num_card = len(given_cards)
loop_end = num_card - 1
fielded_idx = -1
field = "0"
loop_idx = 0
rank = 0

while given_cards.count("0") < num_card:
    while loop_idx != fielded_idx: 
       
        card = given_cards[loop_idx]

        if card_order.index(card) > card_order.index(field):
            fielded_idx = loop_idx
            field = given_cards[loop_idx]
            given_cards[loop_idx] = "0"
            rank += 1
            rank_list[loop_idx] = rank

        loop_idx += 1

        if loop_idx == num_card:
            loop_idx = 0
    
    field = "0"
    loop_idx = loop_idx + 1 if loop_idx < loop_end else 0

for p in rank_list:
    print(str(p))
