from random import randint

class Die:
    """Dice simulation"""

    def __init__(self, numsides=6):
        """Initializes a 6 sided die"""
        self.numsides = numsides
    
    def roll(self):
        """Using the number of sides, roll the dice and return a number."""
        return randint(1, self.numsides)