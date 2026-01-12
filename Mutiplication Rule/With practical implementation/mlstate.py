#ml state space
colors = ["Red", "Green", "Blue"]
shapes = ["Circle", "Square"]
sizes = ["Small", "Medium", "Large"]

state = compound_experiment(colors, shapes, sizes)
print("\nTotal number of states in the ML model:", len(state))
for s in state:
    print(s)

print("done!")
