player_1_start_deck = [
21,
50,
9,
45,
16,
47,
27,
38,
29,
48,
10,
42,
32,
31,
41,
11,
8,
33,
25,
30,
12,
40,
7,
23,
46]

player_2_start_deck = [
22,
20,
44,
2,
26,
17,
34,
37,
43,
5,
15,
18,
36,
19,
24,
35,
3,
13,
14,
1,
6,
39,
49,
4,
28]


def play_round(player_1_card, player_2_card):
    

    if player_1_card > player_2_card: # player 1 wins
        winner = 'player 1'
        return [winner, player_1_card, player_2_card]
    elif player_1_card < player_2_card: # player 2 wins
        winner = 'player 2'
        return [winner, player_2_card, player_1_card]
    else: # tie
        pass # there a no rules for a tie!?!
        
round_memory = {}
round_counter = 0
while (len(player_1_start_deck) > 0) and (len(player_2_start_deck) > 0):
    this_round = [player_1_start_deck, player_2_start_deck]
    if this_round not in round_memory:
        player_1_draw = player_1_start_deck[0]
        player_2_draw = player_2_start_deck[0]
        
        #print(player_1_start_deck)
        player_1_start_deck = player_1_start_deck[1:]
        player_2_start_deck = player_2_start_deck[1:]
        #print(player_1_start_deck)

        round_result = play_round(player_1_draw,player_2_draw)
        #print(round_result)
        if round_result[0] == 'player 1':
            player_1_start_deck.append(round_result[1])
            player_1_start_deck.append(round_result[2])
        elif round_result[0] == 'player 2':
            player_2_start_deck.append(round_result[1])
            player_2_start_deck.append(round_result[2])
        
        round_counter += 1
        round_memory[round_counter] = this_round

    else:
        winner = 'player 1'
        break

# calculate score
if len(player_1_start_deck) == 0:
    winner = 'player 2'
elif len(player_1_start_deck) == 0: #player 1 wins
    winner = 'player 1'

score = 0

if winner == 'player 2':   #player 2 wins
    for index in range(0,len(player_2_start_deck)):
        score += player_2_start_deck[index]*(len(player_2_start_deck) - index)
elif winner == 'player 1':
    for index in range(0,len(player_1_start_deck)):
        score += player_1_start_deck[index]*(len(player_1_start_deck) - index)
print(score)