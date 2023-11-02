def solution():
    # Calculate the number of goats using the number of cows
    goats = 4 * 9  # Mr. Rainwater has 4 times as many goats as cows

    # Calculate the number of chickens using the number of goats
    chickens = goats / 2  # Mr. Rainwater has 2 times as many goats as chickens

    result = chickens
    return result

print(solution())