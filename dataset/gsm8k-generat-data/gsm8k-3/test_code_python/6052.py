def solution():
    """On his farm, Mr. Valentino has 200 chickens, twice as many ducks as chickens and three times as many turkeys as ducks. How many birds does Mr. Valentino have on the farm in total?"""
    # Define the number of chickens
    chickens = 200

    # Calculate the number of ducks and turkeys
    ducks = 2 * chickens
    turkeys = 3 * ducks

    # Calculate the total number of birds on the farm
    total_birds = chickens + ducks + turkeys

    # Display the total number of birds
    result = total_birds
    return result

print(solution())