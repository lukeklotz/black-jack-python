import utils

#keep track of current position and totals
#TODO create class for player hands
playerTotal = 0
dealerTotal = 0

#sets "cards" as the current deck
cards = utils.build_deck()

hit = False

utils.shuffle_deck(cards)
utils.show_deck(cards)

playerHand = utils.player_hand(cards)
dealerHand = utils.dealer_hand(cards)


#clean up / make function for this
print("\n Your hand is:")
print(playerHand)
utils.calculate_hand_total(playerHand, playerTotal)

print("\ndealer hand is:")
print(dealerHand[0])


bust = False
hit = True

playerWin = False
dealerWin = False
tie = False

hit = utils.player_hit(cards, playerHand)
playerTotal = utils.calculate_hand_total(playerHand, playerTotal)

while hit != False or bust != True or playerWin != True:
    if(hit == True):
        print(f"your cards add up to {playerTotal}")
        
        if playerTotal > 21:
            print("Bust!")
            hit = False
            bust = True
            dealerWin = True
            break
        elif playerTotal == 21:
            print("You win!")
            playerWin = True
            break
        elif playerTotal < 21:
            hit = utils.player_hit(cards, playerHand)
            playerTotal = utils.calculate_hand_total(playerHand, playerTotal)

    else:
        print(f"your cards add up to {playerTotal}")
        hit = False
        break


if bust != True:
    while dealerTotal < 17:
        print("dealer hits...")
        dealerHand = utils.dealer_hit(cards, dealerHand)
        dealerTotal = utils.calculate_hand_total(dealerHand, dealerTotal)
        
        if dealerTotal < 17:
            print(f"dealer hand is:{dealerHand}")
            print(f"dealer total is : {dealerTotal}")
        else:
            print(f"dealer hand is:{dealerHand}")
            print(f"dealer total is : {dealerTotal}")
            print("dealer stays")
            
        print(f"dealer hand:{dealerTotal}")
        if dealerTotal >= 17:
            break
else:
    utils.switch_case(playerWin, dealerWin, tie)


utils.isWinner(playerTotal, dealerTotal)


#TODO compare function which determines the winner

 