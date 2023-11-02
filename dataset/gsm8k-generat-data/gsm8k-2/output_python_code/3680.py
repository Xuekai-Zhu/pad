def solution():
    """The leak in Jerry's roof drips 3 drops a minute into the pot he put under it. Each drop is 20 ml, and the pot holds 3 liters. How long will it take the pot to be full?"""
    drip_rate = 3 * 20/1000  # liters per minute
    pot_volume = 3  # liters
    time_to_fill = pot_volume / drip_rate
    result = time_to_fill
    return result

print(solution())