def solution():
    """The leak in Jerry's roof drips 3 drops a minute into the pot he put under it. Each drop is 20 ml, and the pot holds 3 liters. How long will it take the pot to be full?"""
    # Calculate how many drops are needed to fill the pot
    drops_needed = (3 * 1000) / 20 # 3 liters = 3000 ml

    # Calculate how many minutes it will take to fill the pot
    minutes_needed = drops_needed / 3

    # Display the time needed to fill the pot
    result = minutes_needed
    return result

print(solution())