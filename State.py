from Decks import Age1Deck, Age2Deck, Age3Deck
from random import shuffle
class State():
    """
    7 wonders game state

    Game state contains all of the data about a game and provides an interface for changing those datas. Should not direclty change itself.
        that is, this class should define functions for changing itself, but should not call those functions itself.
    """
    def __init__(self, players):
        self.current_age = 1
        self.current_pick = 0
        self.players = players
        self.age_decks = [Age1Deck(len(players)),Age2Deck(len(players)),Age3Deck(len(players))]
        self.is_over = False

    def deal(self):
        """
        shuffles the deck for the current age, resets all packs for all players, and builds 
            packs. Much like a player would build packs during setup. DOES NOT mutate anything.
        """
        shuffle(self.age_decks[self.current_age-1])
        self.packs = [[] for i in range(len(self.players))]
        for i, card in enumerate(self.age_decks[self.current_age-1]):
            self.packs[i % len(self.players)].append(card)

        

    def get_rewards(self):
        for player in self.players:
            pass
        pass

    def direction(self):
        if (self.current_age-1) % 2 == 0: return 1
        else: return -1


    def rotate_hands(self):
        """
        Lets use underscore to represent things that actually change the state
        We might want this in simulator and not state. while it operates on state thats
        outside the scope of this class
        """
        temp_packs = [player.current_hand for player in self.players]
        return temp_packs[self.direction():] + temp_packs[:self.direction()]


    def get_legal_actions(agent):
        return []
        pass

    def set_age(self, age):
        self.age = age

    def get_age(self): return self.age

    def get_player(self, idx): return self.players[idx]

    def get_current_pick(self): return self.current_pick

    def set_current_pick(self, pick): self.current_pick_num = pick

    def age_generator(self):
        for i in range(1,4):
            yield i
            self.next_age()


    def pick_generator(self):
        #alternatively
        for i in range(self.get_pack_size()):
            yield i + 1

    def get_pack_size(self):
        return len(self.age_decks[self.current_age-1]) / len(self.players) 

    def get_cur_age_deck(self):
        return self.age_decks[self.current_age-1]

    def next_age(self):
        self.current_age+=1
        if self.current_age > 3: self.current_age=3

    def copy(self):
        print "WARNING COPY DOES NOTHING IN state.py"
        return self
        
def test():
    state = State(players=range(7)) 
    for i in state.pick_generator():
        print i

if __name__ == "__main__":
    test()
