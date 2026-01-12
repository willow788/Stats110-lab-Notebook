#real world examples

#dice rolling we want to find the probability of getting a sum of 7 when two dice are rolled

dice_1 = [1, 2, 3, 4, 5, 6]
dice_2 = [1, 2, 3, 4, 5, 6]

dice_outcomes = compound_experiment(dice_1, dice_2)

#probability of getting a sum of 7
sum_is_7 = [ o for o in dice_outcomes if o[1] + o[0] == 7]
probability_of_7 = proba_of_outcome(dice_outcomes, sum_is_7)
print("\nProbability of getting a sum of 7 when two dice are rolled:", probability_of_7)
