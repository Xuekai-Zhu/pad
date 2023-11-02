def solution():
    chickens = 200  # Mr. Valentino has 200 chickens
    ducks = 2 * chickens  # He has twice as many ducks as chickens
    turkeys = 3 * ducks  # He has three times as many turkeys as ducks

    # Calculate the total number of birds on the farm
    total_birds = chickens + ducks + turkeys
    result = total_birds
    return result

print(solution())