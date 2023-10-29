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
#TODO implement a card which represents an ACE
#if ACE is in hand and player busts, the value of that card becomes a 1

def shuffle_deck(cards):
    random.shuffle(cards)

def show_deck(cards):
    print(cards)

def player_hand(cards):
    hand = [cards[0], cards[1]]
    del cards[0]
    del cards[0]
    return hand

def dealer_hand(cards):
    dealerHand = [cards[0], cards[1]]
    del cards[0]
    del cards[0]
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


def isWinner(playerTotal, dealerTotal, bust):
    if playerTotal > dealerTotal:
        print("You win!")
    elif bust == True:
        print("You Win!")
    elif playerTotal < dealerTotal:
        print("Dealer wins.")
    else:
        print("Tie!")

def isBust(dealerTotal):
    if dealerTotal > 21:
        return True
    else:
        return False