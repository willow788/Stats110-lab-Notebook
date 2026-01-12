#card( rank x suit) drawing we want to find the probability of drawing a king of hearts from a standard deck of cards

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

card_outcomes = compound_experiment(ranks, suits)

prob_of_king = proba_of_outcome(card_outcomes, [("K", "Hearts")])
print("Probability of getting a king of hearts from a standard deck of cards:", prob_of_king)
