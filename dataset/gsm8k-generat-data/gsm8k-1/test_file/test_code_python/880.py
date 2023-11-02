def solution():
    """Argo has 200 toys. He gives 40 toys to Alyssa, 80 to Bonnie, and 30 to Nicky. How many toys does Argo have now?"""
    starting_toys = 200
    toys_given_alyssa = 40
    toys_given_bonnie = 80
    toys_given_nicky = 30
    toys_remaining = starting_toys - toys_given_alyssa - toys_given_bonnie - toys_given_nicky
    result = toys_remaining
    return result

print(solution())