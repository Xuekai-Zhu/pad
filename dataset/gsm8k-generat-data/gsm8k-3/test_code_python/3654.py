def solution():
    """Philip has a farm with animals. He has 20 cows, 50% more ducks. Philip also has as many pigs as one-fifth of ducks and cows in total. How many animals does Philip have on his farm?"""
    # Define the number of cows and calculate the number of ducks
    cows = 20
    ducks = int(cows * 1.5)

    # Calculate the total number of ducks and cows
    total_animals = cows + ducks

    # Calculate the number of pigs
    pigs = int(total_animals / 5)

    # Calculate the total number of animals
    total_animals += pigs

    # Display the total number of animals
    result = total_animals
    return result

print(solution())