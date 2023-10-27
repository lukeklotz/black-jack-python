import random

def build_deck():
    cards = [2, 2, 2, 2,
             3, 3, 3, 3,
             4, 4, 4, 4,
             5, 5, 5, 5,
             6, 6, 6, 6,
             7, 7, 7, 7,
             8, 8, 8, 8,
             9, 9, 9, 9,
             10,10,10,10]
    return cards

def shuffle_deck(cards):
    random.shuffle(cards)

def show_deck(cards):
    print(cards)

def player_hand(cards):
    hand = [cards[0], cards[1]]
    del cards[0]
    del cards[1]
    return hand

def dealer_hand(cards):
    dealerHand = [cards[0], cards[1]]
    del cards[0]
    del cards[1]
    return dealerHand

def player_hit(cards, playerHand):
    print("Hit?")
    choice = input("Enter Y/N:")
    if choice == "Y":
        playerHand.append(cards[0])
        del cards[0]
        print("Player hand:") # create a function for this
        print(playerHand)
        return True
    elif choice == "N":
        return False
    
def dealer_hit(cards, dealerHand):
    dealerHand.append(cards[0])
    del cards[0]
    return dealerHand

    
def calculate_hand_total(playerHand, playerTotal):
    playerTotal = 0
    for value in playerHand:
        playerTotal += value
    return playerTotal

def switch_case(playerWin, dealerWin, tie):
    if playerWin == True:
        return "You win!"
    elif dealerWin == True:
        return "Dealer wins."
    elif tie == True:
        return "Tie!"
    else:
        return "Error"
    
def isWinner(playerTotal, dealerTotal):
    if playerTotal > dealerTotal:
        return "You win!"
    elif playerTotal < dealerTotal:
        return "Dealer wins."
    else:
        return "Tie!"