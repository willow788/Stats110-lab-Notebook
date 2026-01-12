#probability connection

def proba_of_outcome(total_outcomes,
                     favorable_outcomes):
    """
    total_outcomes: list of all possible outcomes
    favorable_outcomes: list of favorable outcomes
    returns: probability of favorable outcomes
    """
    return len(favorable_outcomes) / len(total_outcomes)

#probability that A2 Occurs in the 2 experiment case

fav_2 = [i for i in outcomes_2 if i[0]=="A2"]
probablity_of_A2_occuring = proba_of_outcome(outcomes_2, fav_2)
print("\nProbability of A2 occuring in 2 experiment case:", probablity_of_A2_occuring)

#probability that B1 and C3 occur in the 3 experiment case
fav_3 = [ i for i in outcomes_3 if(i[1]=="B1" and i[2]=="C3")]
probability_of_B1_C3_occuring = proba_of_outcome(outcomes_3, fav_3)
print("Probability of B1 and C3 occuring in 3 experiment case:", probability_of_B1_C3_occuring)
