def solution():
    """A boy squirrel gathers 6 walnuts and carries them to his burrow in the tree, adding to the 12 already there, and dropping 1 on the way. The girl squirrel brings 5 more walnuts to their burrow and eats 2.  How many walnuts are left?"""
    # Define the initial number of walnuts
    walnuts = 12

    # The boy squirrel adds 6 walnuts and drops 1, leaving the total walnuts to be added as 5
    walnuts += 5

    # The girl squirrel adds 5 walnuts and eats 2, leaving the total walnuts to be added as 3
    walnuts += 3

    result = walnuts
    return result

print(solution())