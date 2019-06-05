class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def print_hand(self, quantity):   
        print(self.name)
        for i in range(quantity):
            print(self.hand[i])



    def get_hand_value(self):
        value =0 
        for i in range(len(self.hand)):
            value += self.hand[i].value

        if value > 21:
            for i in range(len(self.hand)):
                if self.hand[i].face == "Ace":
                    value -= 10


        return value

    def is_bust(self):
        return self.get_hand_value() > 21