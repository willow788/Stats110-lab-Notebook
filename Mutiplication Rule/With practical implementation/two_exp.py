#two experiment case: a  x b

A = ["A1", "A2", "A3"]
B = ["B1", "B2"]

outcomes_2 = compound_experiment(A, B)
print("Total no. of outcomes for 2 experiments:", len(outcomes_2))

length = len(outcomes_2)
for i in range(length):
    print(outcomes_2[i])
