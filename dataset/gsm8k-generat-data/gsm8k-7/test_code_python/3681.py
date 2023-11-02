def solution():
    drops_per_minute = 3
    drop_size = 20  # in ml
    pot_size = 3000  # in ml

    # Calculate the total volume of water that the pot can hold
    total_volume = pot_size

    # Calculate the volume of water that drips into the pot per minute
    volume_per_minute = drops_per_minute * drop_size

    # Calculate the number of minutes it will take the pot to be full
    num_minutes = total_volume / volume_per_minute
    result = num_minutes
    return result

print(solution())