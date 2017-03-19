# File: Blackjack.py
# Description: Program simulates game of blackjack. 
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E 
# Unique Number: 51320
#
# Date Created: 9/19/16
# Date Last Modified: 9/22/16


#create deck class
class Deck():

    def __init__(self):
        self.cardList = ["2C","3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC","KC", "AC",
                         "2D","3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD","KD", "AD",
                         "2H","3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH","KH", "AH",
                         "2S","3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS","KS", "AS"]
    
    #shuffle method
    def shuffle(self):
        import random
        return(random.shuffle(self.cardList))
   
    #string method
    def __str__(self):

        deck_str = ""
            
        for i in range(13):
            deck_str += self.cardList[i].rjust(4)
        
        deck_str += "\n"
        
        for j in range(13, 26):
            deck_str += self.cardList[j].rjust(4)
        
        deck_str += "\n"
        
        for k in range(26, 39):
            deck_str += self.cardList[k].rjust(4)
        
        deck_str += "\n"
        
        for l in range(39, len(self.cardList)):
            deck_str += self.cardList[l].rjust(4)
        
        return deck_str  
        
    #deal card method
    def dealOne(self, player):
        
        #draw card and remove from deck
        draw = self.cardList.pop(0)
        
        #if card dealt is a 10, string has 3 characters; important when assigning pip and suit values to card
        if len(draw) == 3:
            c = Card(draw[0:2], draw[2])
        else:
            c = Card(draw[0], draw[1])
        
        #add drawn card to player's hand
        player.hand.append(draw)
        
        #add value of drawn card to player's hand value
        player.handValue += c.value
        
        
#create card class       
class Card():

    def __init__(self, pip, suit):
        self.pip = pip
        self.suit = suit
        
        if self.pip == "A":
            self.value = 11
        elif self.pip == "K" or self.pip == "Q" or self.pip == "J":
            self.value = 10
        else:
            self.value = int(pip)
        
    #string method       
    def __str__(self):
        return self.pip + self.suit


#create player class
class Player():
    
    def __init__(self):
        self.hand = []
        self.handValue = 0
    
    #string method
    def __str__(self):
        string = ""
        for i in self.hand:
            string = string + i + " "
        return string


#function to show dealer and opponent's hands
def showHands(opp, deal):
    
    print("Dealer shows {} faceup".format(deal.hand[1]))
    print("You show {} faceup".format(opp.hand[1]))
    
    
#function to choose whether to hit or stay
def opponentTurn(cardDeck, dealer, opponent):
    
    #set boolean for presence of ace card in user's hand
    has_ace = False
    
    print("\nYou go first.\n")
 
    #change boolean if user has an ace card hand
    if (opponent.hand[0][0]) == "A" or (opponent.hand[1][0]) == "A":
        has_ace = True
        
        #if user's cards are both aces...
        if (opponent.hand[0][0]) == "A" and (opponent.hand[1][0]) == "A":
            opponent.handValue = 12
            print("Assuming 11 points for an ace, and 1 point for the other ace you were dealt.")
        else:
            print("Assuming 11 points for an ace you were dealt now.")
        
        print("You hold {}for a total of {}.".format(opponent, opponent.handValue))

    
    #if user doesn't have an ace card in hand...       
    else:
        print("You hold {}for a total of {}.".format(opponent, opponent.handValue))
        

    #if user starts with hand value less than 21...
    while opponent.handValue < 21:
        ask = input("1 (hit) or 2 (stay)? " )
        
        #error check if input is a character that isn't a 1 or 2
        while ask.isdigit() == False:
            ask = input("1 (hit) or 2 (stay)? " )
        
        #user decides to hit
        if int(ask) == 1:
            cardDeck.dealOne(opponent)
            print("\nCard dealt: {}".format(opponent.hand[-1]))
            
            #if user's hand value exceed 21 after drawing card...
            if opponent.handValue > 21:
                if has_ace:
                    opponent.handValue -= 10
                    print("Over 21. Switching an ace from 11 points to 1 point.")
                    print("New total: {}\n".format(opponent.handValue))
                    print("You hold {}for a total of {}.".format(opponent, opponent.handValue))

            
            #if user's hand value is still less than 21 after drawing card...
            elif opponent.handValue < 21:
                print("New total: {}\n".format(opponent.handValue))
                print("You hold {}for a total of {}.".format(opponent, opponent.handValue))
        
        #user decides to stay
        elif int(ask) == 2:
            print("Staying with {}.".format(opponent.handValue))
            break
        
        #error check for an input that is an integer not equal to 1 or 2
        else:
            ask = input("1 (hit) or 2 (stay)? " )

            
    #if user starts with hand value greater than 21 and doesn't have an ace card...
    if opponent.handValue > 21 and not has_ace:
        print("You have {}. You bust! Dealer wins.\n".format(opponent.handValue))
    
    #if user has blackjack, whether to begin with or after drawing a card (hand value equals 21)...
    if opponent.handValue == 21:
        print("21!. My turn...")


#function for dealer to hit or stay
def dealerTurn(cardDeck, dealer, opponent):
 
 
    if opponent.handValue > 21:
        return
    
    else:
        
        print("\nDealer's turn")
        print("Your hand: {}for a total of {}".format(opponent, opponent.handValue))
        
        #set boolean for having an ace card to be false
        has_ace = False
        
        #check to see if dealer's starting hand has an ace card
        if (dealer.hand[0][0]) == "A" or (dealer.hand[1][0]) == "A":
            
            #change boolean for having an ace card to be true
            has_ace = True
            
            #if both of dealer's starting cards are aces...
            if (dealer.hand[0][0]) == "A" and (dealer.hand[1][0]) == "A":
                dealer.handValue = 12
                print("Assuming 11 points for an ace, and 1 point for the other ace I have.")
                
            print("Dealer's hand: {}for a total of {} (assuming 11 points for an ace I have).".format(dealer, dealer.handValue))
    
        else:
            print("Dealer's hand: {}for a total of {}".format(dealer, dealer.handValue))

        
        #indicate whether or not an ace card's value was already changed from 11 to 1
        ace_changed = False
        
        #if dealer's hand value is less than user's...
        while dealer.handValue < opponent.handValue:
            cardDeck.dealOne(dealer)
            print("\nDealer hits: {}".format(dealer.hand[-1]))
            print("New total: {}".format(dealer.handValue))

            if dealer.handValue > 21:
                if has_ace and not ace_changed:
                    dealer.handValue -= 10
                    ace_changed = True
                    print("\nOver 21. Switching an ace from 11 points to 1 point.")
                    print("New total: {}".format(dealer.handValue))
            
                #if dealer draws ace card that makes hand value greater than 21, switch value of that card to 1
                elif dealer.hand[-1][0] == "A" and not has_ace:
                    dealer.handValue -= 10
                    print("Over 21. Switching an ace from 11 points to 1 point.")
                    print("New total: {}".format(dealer.handValue))
                
                #if dealer's hand value goes over 21 but already changed value of all existing ace cards
                elif has_ace and ace_changed:
                    break
                
        #if dealer has blackjack, either to begin with or after drawing card...
        if dealer.handValue == 21 or dealer.handValue == opponent.handValue or (dealer.handValue > opponent.handValue and dealer.handValue < 21):
            print("\nDealer has {}. Dealer wins!\n".format(dealer.handValue))
        
        #if dealer has hand value greater than 21...    
        else:
            print("\nDealer has {}. Dealer busts! You win.\n".format(dealer.handValue))

            
def main():
    
    import random
    cardDeck = Deck()

    print("Initial deck:")
    print(cardDeck)
    print()
    
    #random.seed(50)
    cardDeck.shuffle()
    print("Shuffled deck:")
    print(cardDeck)
    print()
    
    dealer = Player()
    opponent = Player()
    
    cardDeck.dealOne(opponent)
    cardDeck.dealOne(dealer)
    cardDeck.dealOne(opponent)
    cardDeck.dealOne(dealer)
    
    print("Deck after dealing two cards each:")
    print(cardDeck)
    print()
    
    showHands(opponent, dealer)
    opponentTurn(cardDeck, dealer, opponent)
    dealerTurn(cardDeck, dealer, opponent)
    
    print ("Game over.")
    print ("Final hands:")
    print ("   Dealer:   ", dealer)
    print ("   You:      ", opponent)
    
main()