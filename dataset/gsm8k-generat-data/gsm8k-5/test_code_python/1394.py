def solution():
    ducks = 150  # Jen has 150 ducks
    ducks_per_chicken = 4  # Jen has 10 more ducks than 4 times the number of chickens
    chickens = (ducks - 10) / ducks_per_chicken  # Solve for the number of chickens
    total_birds = chickens + ducks  # Calculate the total number of birds
    result = total_birds
    return result

print(solution())