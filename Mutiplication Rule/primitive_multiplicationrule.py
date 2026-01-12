def compound_experiment(a, b):
    outcomes = []

    for i in range(1,a+1):
        for j in range(1,b+1):
            outcomes.append((f"A{i}", f"B{j}"))

        return outcomes
    

# Example usage
results = compound_experiment(3, 2)
print("Compound Experiment Outcomes:")
for outcome in results:
    print(outcome)
    

    
