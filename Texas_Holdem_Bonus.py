import random

deck = ["2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ah",
        "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd", "Ad",
        "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "As",
        "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ac"]

card_value = {"A": 13,
             "K": 12,
             "Q": 11,
             "J": 10,
             "T": 9,
             "9": 8,
             "8": 7,
             "7": 6,
             "6": 5,
             "5": 4,
             "4": 3,
             "3": 2,
             "2": 1,}

value_card = {13: 'A',
              12: 'K',
              11: 'Q',
              10: 'J',
              9: 'T',
              8: '9',
              7: '8',
              6: '7',
              5: '6',
              4: '5',
              3: '4',
              2: '3',
              1: '2'}

hand_name = {9: "Straight Flush",
             8: "Four-of-a-kind",
             7: "Full House",
             6: "Flush",
             5: "Straight",
             4: "Three-of-a-kind",
             3: "Two Pair",
             2: "Pair",
             1: "High Card"}


def shuffle_deck():
    global deck
    for i in xrange(15):
        random.shuffle(deck)


def split_cards(cards):
    #Set variables
    sorted_hand = []
    values = []
    suits = []
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

    #Order the cards based on the above order
    for order_card in order:
        for hand_card in cards:
            if order_card == hand_card[0]:
                sorted_hand.append(hand_card)

    #Split the ordered hand into values and suits
    for i in xrange(7):
        values.append(card_value[sorted_hand[i][0]])
        suits.append(sorted_hand[i][1])

    return values, suits


def get_hand_info(cards):
    global value_card
    values, suits = split_cards(cards)
    hand_info = {"Hand Value": 0,
                 "Primary Value": 0,
                 "Secondary Value": 0,
                 "Kickers": [],
                 "Description": ""}

    #Determine if straight flush
    for i, start_val in enumerate(values):
        if i > 2:
            break
        flush_count = 1
        flush_suit = suits[i]
        for diff in xrange(1,5):
            if start_val - diff not in values:
                break
            #Need this loop since there may be more than 1 of a value, so we need to check suit of all
            for x, check_suit in enumerate(suits):
                if values[x] == start_val - diff and check_suit == flush_suit:
                    flush_count += 1
        else:
            if flush_count == 5:
                hand_info["Hand Value"] = 9
                hand_info["Primary Value"] = start_val
                hand_info["Secondary RValue"] = "N/A"
                hand_info["Kickers"] = "N/A"
                hand_info["Description"] = 'straight flush up to a %s! Incredible!' % value_card[start_val]
                return hand_info

    #Determine if Four-of-a-kind
    for i, quads in enumerate(values):
        if i > 3:
            break
        if values.count(quads) == 4:
            hand_info["Hand Value"] = 8
            hand_info["Primary Value"] = quads
            hand_info["Secondary Value"] = "N/A"
            for kicker in values:
                if kicker != quads:
                    hand_info["Kickers"] = [kicker]
                    break
            hand_info["Description"] = "four-of-a-kind of %s's with a %s kicker!" % (value_card[quads],
                                                                                     value_card[kicker])
            return hand_info

    #Determine if Full House
    for trips in values:
        if values.count(trips) == 3:
            for pair in values:
                if values.count(pair) == 2:
                    hand_info["Hand Value"] = 7
                    hand_info["Primary Value"] = trips
                    hand_info["Secondary Value"] = pair
                    hand_info["Kickers"] = "N/A"
                    hand_info["Description"] = "full house: %s's full of %s's!" % (value_card[trips],
                                                                                   value_card[pair])
                    return hand_info

    #Determine if Flush
    for i, suit in enumerate(suits):
        if suits.count(suit) >= 5:
            hand_info["Hand Value"] = 6
            hand_info["Primary Value"] = values[i]
            hand_info["Secondary Value"] = "N/A"
            for j in xrange(i+1, 7):
                if suits[j] == suit:
                    hand_info["Kickers"].append(values[j])
                if len(hand_info["Kickers"]) == 4:
                    break
            hand_info["Description"] = "%s high flush!" % value_card[hand_info["Primary Value"]] #TOD O: ADD KICKERS!
            return hand_info

    #Determine if Straight
    for i, start_val in enumerate(values):
        if i > 2:
            break
        for diff in xrange(1,5):
            if start_val - diff not in values:
                break
        else:
            hand_info["Hand Value"] = 5
            hand_info["Primary Value"] = start_val
            hand_info["Secondary Value"] = "N/A"
            hand_info["Kickers"] = "N/A"
            hand_info["Description"] = "straight up to a %s!" % value_card[start_val]
            return hand_info

    #Determine if Three-of-a-kind
    for i, trips in enumerate(values):
        if i > 4:
            break
        if values.count(trips) == 3:
            hand_info["Hand Value"] = 4
            hand_info["Primary Value"] = trips
            hand_info["Secondary Value"] = "N/A"
            for kicker in values:
                if kicker != trips:
                    hand_info["Kickers"].append(kicker)
                if len(hand_info["Kickers"]) == 2:
                    break
            hand_info["Description"] = "three-of-a-kind of %s's!" % value_card[trips]
            return hand_info

    #Determine if Two Pair
    for primary_pair in values:
        if values.count(primary_pair) == 2:
            for secondary_pair in values:
                if values.count(secondary_pair) == 2 and secondary_pair != primary_pair:
                    hand_info["Hand Value"] = 3
                    hand_info["Primary Value"] = primary_pair
                    hand_info["Secondary Value"] = secondary_pair
                    for kicker in values:
                        if kicker != primary_pair and kicker != secondary_pair:
                            hand_info["Kickers"] = [kicker]
                            break
                    hand_info["Description"] = "two pair: %s's and %s's with a %s kicker!" % (value_card[primary_pair],
                                                                                              value_card[secondary_pair],
                                                                                              value_card[kicker])
                    return hand_info

    #Determine if Pair
    for pair in values:
        if values.count(pair) == 2:
            hand_info["Hand Value"] = 2
            hand_info["Primary Value"] = pair
            hand_info["Secondary Value"] = "N/A"
            for kicker in values:
                if kicker != pair:
                    hand_info["Kickers"].append(kicker)
                if len(hand_info["Kickers"]) == 3:
                    break
            hand_info["Description"] = "pair of %s's!" % value_card[pair]
            return hand_info

    #Anything else is high card
    hand_info["Hand Value"] = 1
    hand_info["Primary Value"] = "N/A"
    hand_info["Secondary Value"] = "N/A"
    hand_info["Kickers"] = values[:5]
    hand_info["Description"] = 'high card of %s!' % value_card[values[0]]

    return hand_info


def print_hand(hand_num, bankroll, ante_bet="", flop_bet="", turn_bet="", river_bet="",
               player_hand="", dealer_hand="", community_cards=""):
    if ante_bet == "":
        print "_____________________NEW_HAND_____________________"
    print 'Hand #: %s' % hand_num
    print 'Bankroll: $%s' % bankroll
    print ''
    print "Your hand:",
    for card in player_hand:
        print card,
    print ''
    print ''
    print "Community cards:",
    for card in community_cards:
        print card,
    print ''
    print ''
    print "Dealer's hand:",
    for card in dealer_hand:
        print card,
    print ''
    print ''
    print 'Ante bet: %s' % ante_bet
    print 'Flop bet: %s' % flop_bet
    print 'Turn bet: %s' % turn_bet
    print 'River bet: %s' % river_bet
    print ''


def print_intro():
    print "               W e l c o m e   t o                "
    print "      T e x a s   H o l d e m   B o n u s !       "
    print "                     ______________               "
    print "                    |A             |              "
    print "             _______|______        |              "
    print "            |A             |       |              "
    print "            |              |       |              "
    print "            |              |       |              "
    print "            |              |       |              "
    print "            |              |       |              "
    print "            |              |_______|              "
    print "            |              |                      "
    print "            |______________|                      "
    print "                                                  "
    print "           Created By: Andrew Phillips            "
    print "            (press enter to continue)             "
    raw_input()
    print 'You will start with $200.'
    print ''
    print 'The game will proceed in the following steps:'
    print '    1. You will be asked for your ante ($5 minimum), and then you will see your cards'
    print '    2. After viewing your cards, enter "p" to play for 2x the ante, or "f" to fold and lose your ante'
    print '    3. The flop will come, and you may enter "b" to bet the ante amount or "c" to check'
    print '    4. The turn will come, and you may enter "b" to bet the ante amount or "c" to check'
    print '    5. The river will come, and the dealer will be dealt his cards'
    print '    6. A winning hand will pay 1-to-1 for all non-ante bets except straights or higher, which include antes'
    print '    7. You will enter "d" to deal a new hand or "q" to quit'
    print ''
    print 'Cards are displayed in the form (value)(suit)'
    print '    Ex: Ah = Ace of hearts'
    print '        Tc = Ten of clubs'
    print '        9d = 9 of diamonds'
    print '        etc.'
    print ''
    print 'Press enter to start your first hand!'
    print ''
    raw_input()


def run_game():
    global hand_name
    print_intro()
    bankroll = 200
    hand_num = 1
    while True:
        #Set up hand
        player_hand = []
        dealer_hand = []
        community_cards = []
        print_hand(hand_num=hand_num, bankroll=bankroll)
        shuffle_deck()

        #Get ante bet
        while True:
            while True:
                try:
                    ante_bet = int(raw_input('Enter ante amount (integer >= 5): '))
                except:
                    print "You must enter an integer!"
                else:
                    break
            if ante_bet >= 5 and ante_bet*3 <= bankroll:
                bankroll -= ante_bet
                break
            if ante_bet*3 > bankroll: print 'Too large of an ante!'
            elif ante_bet < 5: print 'Too small of an ante!'
            else: print 'Invalid entry!'
        print ''

        #Deal and display hand
        player_hand.append(deck[0])
        player_hand.append(deck[1])
        print_hand(hand_num=hand_num, bankroll=bankroll,
                   ante_bet=ante_bet, player_hand=player_hand)

        #Determine if playing, then deal or begin new hand
        while True:
            play = raw_input('Would you like to play this hand? (p to play, f to fold): ').lower()
            if play == 'p' or play == 'f':
                break
            print 'Invalid entry!'
        print ''
        if play == 'f':
            print 'You chose to fold! You lose your ante of $%s' % ante_bet
        else:
            #Deal flop, adjust bankroll, etc.
            flop_bet = ante_bet*2
            bankroll -= flop_bet
            community_cards.append(deck[3])
            community_cards.append(deck[4])
            community_cards.append(deck[5])
            print_hand(hand_num=hand_num, bankroll=bankroll,
                       ante_bet=ante_bet, player_hand=player_hand,
                       flop_bet=flop_bet, community_cards=community_cards)

            #Bet or check the turn, then adjust bankroll and deal
            while True:
                if bankroll < ante_bet:
                    print "You don't have enough money to bet!"
                    turn_move = 'c'
                    break
                turn_move = raw_input('Would you like to bet the turn? (b to bet, c to check): ').lower()
                if turn_move == 'b' or turn_move == 'c':
                    break
                print 'Invalid entry!'
            print ''
            if turn_move == 'b':
                turn_bet = ante_bet
                bankroll -= turn_bet
            else:
                turn_bet = 0
            community_cards.append(deck[7])
            print_hand(hand_num=hand_num, bankroll=bankroll,
                       ante_bet=ante_bet, player_hand=player_hand,
                       flop_bet=flop_bet, community_cards=community_cards,
                       turn_bet=turn_bet)

            #Bet or check the river, then adjust the bankroll and deal last card and dealer's cards
            while True:
                if bankroll < ante_bet:
                    print "You don't have enough money to bet!"
                    river_move = 'c'
                    break
                river_move = raw_input('Would you like to bet the river? (b to bet, c to check): ').lower()
                if river_move == 'b' or river_move == 'c':
                    break
                print 'Invalid entry!'
            print ''
            if river_move == 'b':
                river_bet = ante_bet
                bankroll -= river_bet
            else:
                river_bet = 0
            community_cards.append(deck[9])
            dealer_hand.append(deck[10])
            dealer_hand.append(deck[11])
            print_hand(hand_num=hand_num, bankroll=bankroll,
                       ante_bet=ante_bet, player_hand=player_hand,
                       flop_bet=flop_bet, community_cards=community_cards,
                       turn_bet=turn_bet, river_bet=river_bet,
                       dealer_hand=dealer_hand)

            #Determine the winner
            player_hand.extend(community_cards)
            dealer_hand.extend(community_cards)
            player_result = get_hand_info(player_hand)
            dealer_result = get_hand_info(dealer_hand)
            print 'You have a %s' % player_result['Description']
            print 'The dealer has a %s' % dealer_result['Description']
            print ''
            winner = 'Dealer'
            if player_result["Hand Value"] > dealer_result['Hand Value']:
                winner = 'Player'
            elif player_result["Hand Value"] == dealer_result['Hand Value']:
                if player_result["Primary Value"] > dealer_result['Primary Value']:
                    winner = 'Player'
                elif player_result["Primary Value"] == dealer_result['Primary Value']:
                    if player_result["Secondary Value"] > dealer_result['Secondary Value']:
                        winner = 'Player'
                    elif player_result["Secondary Value"] == dealer_result['Secondary Value']:
                        if player_result["Kickers"] == dealer_result["Kickers"]:
                            winner = 'Draw'
                        for i in xrange(len(player_result["Kickers"])):
                            if player_result["Kickers"][i] > dealer_result["Kickers"][i]:
                                winner = 'Player'

            #Below: change format so that winnings are printed, maybe even new bankroll
            bet_sum = ante_bet + flop_bet + turn_bet + river_bet
            if winner == 'Draw':
                print 'You and the dealer tied! The player is returned his bets of $%s.' % bet_sum
                bankroll += bet_sum
            elif winner == 'Player':
                print 'You beat the dealer!',
                if player_result["Hand Value"] >= 5:
                    print 'You won $%s!' % (bet_sum)
                    bankroll += (bet_sum*2)
                else:
                    print 'You won $%s!' % (bet_sum-ante_bet)
                    bankroll += ((bet_sum*2)-ante_bet)
            else:
                print 'The dealer wins! You lose $%s.' % bet_sum
        print ''
        print '----------------------------------------------------------'
        print 'After %s hands, your bankroll is $%s.' % (hand_num, bankroll)
        while True:
            deal = raw_input("Play again? (d to deal, q to quit): ").lower()
            if deal == 'd' or deal == 'q':
                break
            print 'Invalid entry!'
        if deal == 'q' or bankroll < 15:
            break
        else:
            hand_num += 1

    print ''

    #Summarize the game
    if bankroll < 15:
        print "Game over, you ran out of money!"
        print "Better luck next time!"
    elif bankroll < 200:
        print "You left the game at -$%s." % (200-bankroll)
        print "Better luck next time!"
    elif bankroll == 200:
        print "You left the game exactly how you started!"
        print "Come play again!"
    else:
        print "Congratulations, you won $%s!" % (bankroll-200)
        print "Come play again!"


def run_sim(num_sims):
    global deck

    hand_count = {"Straight Flush": 0,
                  "Four-of-a-kind": 0,
                  "Full House": 0,
                  "Flush": 0,
                  "Straight": 0,
                  "Three-of-a-kind": 0,
                  "Two Pair": 0,
                  "Pair": 0,
                  "High Card": 0,
                  }

    player_cards = [0,1,3,4,5,7,9]
    dealer_cards = [3,4,5,7,9,10,11]

    for i in xrange(num_sims):
        player_hand = []
        dealer_hand = []
        shuffle_deck()
        for num in player_cards:
            player_hand.extend([deck[num]])
        for num in dealer_cards:
            dealer_hand.extend([deck[num]])
        player_result = get_hand_info(player_hand)
        dealer_result = get_hand_info(dealer_hand)
        hand_count[hand_name[player_result["Hand Value"]]] += 1
        hand_count[hand_name[dealer_result["Hand Value"]]] += 1

    for key in hand_count.keys():
        hand_count[key] /= float(num_sims)*2

    print 'Simulation Results:'
    print ''
    print "Straight Flush:", hand_count["Straight Flush"]
    print "Four-of-a-kind:", hand_count["Four-of-a-kind"]
    print "Full House:", hand_count["Full House"]
    print "Flush:", hand_count["Flush"]
    print "Straight:", hand_count["Straight"]
    print "Three-of-a-kind:", hand_count["Three-of-a-kind"]
    print "Two Pair:", hand_count["Two Pair"]
    print "Pair:", hand_count["Pair"]
    print "High Card:", hand_count["High Card"]


if __name__ == "__main__":
    run_game()
    #run_sim(100)




