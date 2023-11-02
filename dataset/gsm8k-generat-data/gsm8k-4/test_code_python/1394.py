def solution():
    """Jen has 10 more ducks than four times the number of chickens. If Jen has 150 ducks, how many total birds does she have?"""
    # Set the number of ducks that Jen has
    ducks = 150

    # Calculate the number of chickens using the given information about ducks
    chickens = (ducks - 10) / 4

    # Calculate the total number of birds
    total_birds = ducks + chickens

    # Return the result
    result = total_birds
    return result

print(solution())