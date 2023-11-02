def solution():
    # Define the number of chickens
    chickens = 200

    # Define the number of ducks (twice as many as chickens)
    ducks = 2 * chickens

    # Define the number of turkeys (three times as many as ducks)
    turkeys = 3 * ducks

    # Calculate the total number of birds on the farm
    total_birds = chickens + ducks + turkeys
    result = total_birds
    return result

print(solution())