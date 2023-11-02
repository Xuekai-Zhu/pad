def solution():
    """On his farm, Mr. Valentino has 200 chickens, twice as many ducks as chickens and three times as many turkeys as ducks. How many birds does Mr. Valentino have on the farm in total?"""
    # Define the number of chickens
    chickens = 200

    # Define the number of ducks
    ducks = chickens * 2

    # Define the number of turkeys
    turkeys = ducks * 3

    # Calculate the total number of birds
    total_birds = chickens + ducks + turkeys

    result = total_birds
    return result

print(solution())