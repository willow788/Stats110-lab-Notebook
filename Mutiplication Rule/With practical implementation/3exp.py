#three experiment case: a x b x c
C = ["C1", "C2", "C3", "C4"]

outcomes_3  = compound_experiment(A, B, C)
print("\nTotal no. of outcomes for 3 experiments:", len(outcomes_3))
length = len(outcomes_3)
for i in range(length):
    print(outcomes_3[i])
