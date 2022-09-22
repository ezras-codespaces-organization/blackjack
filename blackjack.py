# super basic review of OOP in Python 

from random import shuffle 
# import typing 
from typing import List 

class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit: str, value: str):
        self.suit = suit # should be one of ["Diamonds", "Spades", "Hearts", "Clubs"] 
        self.value = value # should be one of ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    # Returns the suit of the card.
    def get_suit(self) -> str:
        return self.suit 

    # Returns the value of the card.
    def get_value(self) -> str:
        return self.value 
        
    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"
      

class Deck:
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
    VALUES = ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    def __init__(self):
        #self.deck = [(suit, value) for suit in SUITS for value in VALUES]
        # map_values_sense = {"Two": 0, "Three":1, "Four":2, "Five":3, "Six":4, "Seven":5, "Eight":6, "Nine":7, "Ten":8, \ 
        #                     "Jack":9, "Queen":10, "King":11, "Ace":12}
        #self.shuffle(self.deck) # in place; uses python built-in `shuffle` from `random` `import`ed above 
        self.reset() 

    # Returns the number of Cards in the Deck
    def size(self) -> int:
        return len(self.deck) 
    
    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self) -> None: # to me it seems like horrible 'form' to use the same name as a built-in, absolutely atrocious, i never do this!
        shuffle(self.deck)  # in place; uses python built-in `shuffle` from `random` `import`ed above  
    
    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self) -> Card: 
        return self.deck[-1] 

    def __len__(self):
        return len(self.deck) 
    
    def __getitem__(self, sliced):
        return self.deck[sliced] 
    
    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self) -> Card:
        card = self.deck.pop() 
        return card 
    
    # Adds the input card to the deck. 
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card: Card) -> None:
        if len(self.deck) >= 52: # presumably the above comment means *inclusively* when it says "more than" 
            raise Exception('deck already full') 
        else:
            self.deck.append(card) # let's see is a deck of cards a stack? idk, i don't play cards...  
    
    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self) -> None:
        for card in self.cards: # Um, note to self: there's no self.cards...  
            print (card) 
      
    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self) -> None:
        self.deck = [Card(suit, value) for suit in self.SUITS for value in self.VALUES]
        self.shuffle() 

class Blackjack:
    # Creates a Blackjack game with a new Deck.
    def __init__(self):
        # When implementing Blackjack you'll want to have a few instance variables.
        self.deck = Deck() # 1. The current deck (Deck object) 
        self.discard = [] # 2. The discard pile (List of Cards)
        self.hand = [] # 3. The current hand (List of Cards) 
        # Together all of these should add up to a full deck (totalling 52 cards) 
        self.deal_new_hand() # create a `self.hand` holding the hand of cards for duration of one game  
    
    # Computes the score of a hand. 
    # For examples of hands and scores as a number. 
    # 2,5 -> 7
    # 3, 10 -> 13
    # 5, King -> 15
    # 10, Ace -> 21
    # 10, 8, 4 -> Bust so return -1
    # 9, Jack, Ace -> 20 
    # If the Hand is a bust return -1 (because it always loses)
    def _get_score(self, hand: List[Card]) -> int:
        if hand: # was formerly for debugging... 
            pass 
            # print (type(hand[0]))
            # print (hand[0]) 
            # print ('------------------------')
            # print () 
        total = 0 
        count_aces = 0 
        for card in hand: 
            if card.value != 'Ace': 
                total += self.score_card(card) 
                
            else: 
                count_aces += 1 
        if count_aces: 
            if count_aces == 1: 
                if total + 11 <= 21: 
                    total += 11 
                else:
                    total += 1 
            else: # 2, 3, or 4 aces. Only possibly can score max 1 of them as an 11, the rest have to be 1s. 
                if count_aces == 2: 
                    if total + 12 <= 21:
                        total += 12 
                    else: 
                        total += 2 
                else: # count_aces is either 3 or 4 
                    total += (count_aces - 1) # only possibly max 1 ace will be scored as an 11 hence the minus 1 
                    if total + 11 <= 21:
                        total += 11
                    else: 
                        total += 1 
        return total  

    # return score of any card other than an Ace which is handled with a crap ton of ugly logic separately "aces sold separately"
    # "we don't deal with aces" 
    def score_card(self, card: Card) -> int: 

        scores_of_cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, \
                            'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King':10}

        # print ("string object is not callable???")
        # print (type(card))
        # print (card)
        # suit = card.get_suit()
        value = card.get_value() 
        return scores_of_cards[value] 
  
    # Prints the current hand and score.
    # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
    # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
    def _print_current_hand(self) -> None:
        # pass
        if not self.hand:
            print ("no hand!") 
        else:
            for card in self.hand:
                print (card) 


    # The previous hand is discarded and shuffled back into the deck.
    # Should remove the top 2 cards from the current deck and 
    # Set those 2 cards as the "current hand". 
    # It should also print the current hand and score of that hand.
    # If less than 2 cards are in the deck, 
    # then print an error instructing the client to shuffle the deck.
    def deal_new_hand(self) -> None:
        if len(self.deck) < 2: 
            print ("Error: deck to skinny--reshuffle first!") 
        else: 
            if self.hand:
                # print ()
                # print (self.hand)
                # print (len(self.hand)) 
                # print ()  
                for each_card in self.hand[:]: # um, that `[:]` is a big deal, how can i remember to never make this mistake again?!?
                    self.hand.remove(each_card) 
                    #self.deck.append(each_card)
                    self.discard.append(each_card)
                # print ()
                # print (self.discard)
                # print (len(self.discard))
                # print () 
                self.shuffle() 
                #self.reshuffle() 
            new_hand = self.deck[-2:] # implemented slicing in __getitem__ maybe this will work now? 
            self.deck = self.deck[:-2]
            self.hand = new_hand 
            print ("Current hand:")
            print (self.hand) # It should also print the current hand and score of that hand. 
            # Current hand:
            # [<__main__.Card object at 0x7f7f107a10a0>, <__main__.Card object at 0x7f7f1079c640>]
            self._print_current_hand()
            print (self._get_score(self.hand)) 


    
    # Deals one more card to the current hand and prints the hand and score.
    # If no cards remain in the deck, print an error.
    def hit(self) -> None: 
        if len(self.deck) < 1:
            print ("Error")
        else: 
            self.hand.append(self.deck[-1])
            self.deck = self.deck[:-1] 
    
    def size(self) -> int: 
        return len(self.deck) 
    
    def discard_size(self) -> int:
        return len(self.discard) 
    
    def hand_size(self) -> int: 
        return len(self.hand) 

    # keeps the discard pile separate (there's no hand anymore a.t.m.) 
    # and just reshuffles... only the deck 
    def shuffle(self) -> None: 
        # print (self.deck) 
        # print ()
        # print (len(self.deck)) 
        # print () 
        # print (len(self.discard)) 
        # print () 
        # print () 
        # print ('prior to shuffle:')
        # print (self.deck[:4])
        # print ()
        # print (len(self.deck))
        # print () 
        # q = self.deck[:] 
        shuffle(self.deck) # python3 built-in `shuffle`s in place & `return`s None  
        # print () 
        # print ('post shuffle:')
        # print (self.deck[:4]) # sanity check 
        # print ()
        # print (len(self.deck))
        # print ()
        # print (set(q) == set(self.deck)) # sanity check 
        


    # Reshuffles all cards in the "current hand" and "discard pile"
    # and shuffles everything back into the Deck.
    def reshuffle(self) -> None:
        # pass 
        # presently it isn't clear to me what the discard pile is or when it would ever be used 
        # however the deal is, from the instructions, that the discard pile + the hand + the deck == a 52 card deck 
        #deck = self.hand[:] + self.discard[:] + self.deck[:] # not sure it is ever a good idea to use `+` on lists in python, hmmmm...
        
        
        # what i used to do (for the entirety of this method) before i understood how discard is supposed to used --->  
        self.deck = Deck() # ---^--- seems like if i continued that idea i would be re-implementing logic that exists elsewhere 
        self.hand = [] 
        self.discard = [] # okay everything is reset... now `reshuffle` is exactly the same logic as `Blackjack()` right? :-( 


# Initializes a new deck. The "current_hand" is empty. 
blackjack = Blackjack()  

print ()
print ("how big is the deck?")
print (blackjack.size())
print () 
print ("how big is the discard pile?")
print (blackjack.discard_size()) 
print () 
print ("how big is the current hand?")
print (blackjack.hand_size())
print () 
print ('-----------------------------------------------')
print () 

blackjack.deal_new_hand() 
'''
Removes top 2 cards from deck and moves them to the current hand.
Prints the hand and the score of that hand.

For example would print out.
Note this is just an example, since the deck is shuffled, any 2 cards could come out.

("4 of Clubs", "9 of Diamonds", 13)

Here the 4 of Clubs and 9 of Diamonds would be removed from the Deck and 
would be the current hand. Discard pile is empty.
'''

print ()
print ("how big is the deck?")
print (blackjack.size())
print () 
print ("how big is the discard pile?")
print (blackjack.discard_size()) 
print () 
print ("how big is the current hand?")
print (blackjack.hand_size())
print () 

blackjack.deal_new_hand()
'''
The previous current hand (4 of Clubs and 9 of Diamonds) is added to the discard pile
and NOT added back into the deck.

A new 2 cards are dealt into the current hand, for example.

("7 of Spades", "5 of Hearts", 12)

Now the Deck has 48 cards as 2 are in the discard pile and 2 are in the curent hand.
'''

# sanity check to the foregoing: 
print ()
print ("how big is the deck?")
print (blackjack.size())
print () 
print ("how big is the discard pile?")
print (blackjack.discard_size()) 
print () 
print ("how big is the current hand?")
print (blackjack.hand_size())
print () 

# seneca_wolf@seneca_wolf:/mnt/c/Users/ezras/Dropbox/PC (2)/Desktop/coachable/black_jack_codespaces_0$ !py
# python3 blackjack.py
# Current hand:
# [<__main__.Card object at 0x7f5db9a6c9a0>, <__main__.Card object at 0x7f5db99fb8b0>]
# Ace of Diamonds
# Eight of Diamonds
# 19
# Current hand:
# [<__main__.Card object at 0x7f5db99d8f70>, <__main__.Card object at 0x7f5db99fb6a0>]
# Four of Clubs
# Six of Diamonds
# 10
# Current hand:
# [<__main__.Card object at 0x7f5db99d8b50>, <__main__.Card object at 0x7f5db99d8790>]
# Six of Hearts
# Nine of Spades
# 15

# how big is the deck?
# 46

# how big is the discard pile?
# 4

# how big is the current hand?
# 2

# seneca_wolf@seneca_wolf:/mnt/c/Users/ezras/Dropbox/PC (2)/Desktop/coachable/black_jack_codespaces_0$






