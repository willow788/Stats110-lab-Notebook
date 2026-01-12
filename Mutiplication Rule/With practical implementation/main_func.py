from itertools import product

def compound_experiment(*experiment):
    """
    experiment: list of outcomes for each sub-experiment
    returns: list of all the values representing the compound experiment
   
    """
    return list(product(*experiment))
