def solution():
    """The leak in Jerry's roof drips 3 drops a minute into the pot he put under it. Each drop is 20 ml, and the pot holds 3 liters. How long will it take the pot to be full?"""
    drops_per_minute = 3
    ml_per_drop = 20
    liters_in_pot = 3
    ml_in_pot = liters_in_pot * 1000
    drops_needed = ml_in_pot / ml_per_drop
    time_to_fill = drops_needed / drops_per_minute
    result = time_to_fill
    
    return result

print(solution())