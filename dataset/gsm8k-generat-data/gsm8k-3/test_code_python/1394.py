def solution():
    """Jen has 10 more ducks than four times the number of chickens. If Jen has 150 ducks, how many total birds does she have?"""
    # Define the variables
    ducks = 150
    chickens = (ducks - 10) / 4
    total_birds = ducks + chickens

    # Display the total number of birds
    result = total_birds
    return result

print(solution())