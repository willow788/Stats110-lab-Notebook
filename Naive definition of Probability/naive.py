class NaiveSampleSpace():
    def __init__(self, outcomes):
        """
        outcomes: a list of possible outcomes
        example: ['H', 'T'] for a coin flip
        example: [1, 2, 3, 4, 5, 6] for a die roll
       
        """
        self.outcomes = list(outcomes)
        self.n = len(outcomes)

        if self.n == 0:
            raise ValueError ("Sample space must have at least one outcome.")
        

    def probability(self, event):
        """
        event: set of possible outcomes

        
        """
        favourable_outcomes = 0
        for outcome in event:
            if outcome in self.outcomes:
                favourable_outcomes += 1

        return favourable_outcomes / self.n
        
    def support(self):
        """
        returns the list of all possible outcomes
        """
        return self.outcomes
    

# Example usage:
if __name__ == "__main__":
    coin = NaiveSampleSpace(['H', 'T'])
    print("Coin flip outcomes:", coin.support())
    print("Probability of heads:", coin.probability(['H']))
    print("Probability of tails:", coin.probability(['T']))
    print("Probability of heads or tails:", coin.probability(['H', 'T']))

    die = NaiveSampleSpace([1, 2, 3, 4, 5, 6])
    print("Die roll outcomes:", die.support())
    print("Probability of rolling a 3:", die.probability([3]))
    print("Probability of rolling an even number:", die.probability([2, 4, 6]))
