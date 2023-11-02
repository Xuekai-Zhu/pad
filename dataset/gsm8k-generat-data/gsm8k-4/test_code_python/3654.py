def solution():
    """Philip has a farm with animals. He has 20 cows, 50% more ducks. Philip also has as many pigs as one-fifth of ducks and cows in total. How many animals does Philip have on his farm?"""
    # Define the number of cows
    cows = 20

    # Calculate the number of ducks, which is 50% more than the number of cows
    ducks = cows * 1.5

    # Calculate the total number of cows and ducks
    total_cows_ducks = cows + ducks

    # Calculate the number of pigs, which is one-fifth of the total number of cows and ducks
    pigs = total_cows_ducks / 5

    # Calculate the total number of animals on the farm
    total_animals = cows + ducks + pigs

    # Return the result
    result = total_animals
    return result

print(solution())