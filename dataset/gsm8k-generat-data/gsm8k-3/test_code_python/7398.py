def solution():
    """A boy squirrel gathers 6 walnuts and carries them to his burrow in the tree, adding to the 12 already there, and dropping 1 on the way. The girl squirrel brings 5 more walnuts to their burrow and eats 2.  How many walnuts are left?"""
    # Calculate the number of walnuts after the boy squirrel's collection
    boy_collection = 6
    boy_dropped = 1
    initial_walnuts = 12
    total_walnuts = initial_walnuts + boy_collection - boy_dropped

    # Calculate the number of walnuts after the girl squirrel's contribution
    girl_contribution = 5
    girl_eats = 2
    total_walnuts += girl_contribution - girl_eats

    # Display the total number of walnuts left
    result = total_walnuts
    return result

print(solution())