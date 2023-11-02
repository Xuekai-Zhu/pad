def solution():
    # Calculate the number of drops needed to fill the pot
    pot_volume = 3 # in liters
    pot_volume_milliliter = pot_volume * 1000 # in milliliters
    drop_volume = 20 # in milliliters
    drops_needed = pot_volume_milliliter // drop_volume # integer division

    # Calculate the time needed to fill the pot in minutes
    leak_rate = 3 # drops per minute
    time_needed = drops_needed // leak_rate # integer division

    result = time_needed
    return result

print(solution())