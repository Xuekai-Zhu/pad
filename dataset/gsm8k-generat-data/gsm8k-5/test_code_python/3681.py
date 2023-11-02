def solution():
    drops_per_minute = 3  # The leak drips 3 drops per minute
    volume_per_drop = 20  # Each drop is 20 ml
    pot_capacity = 3000  # The pot holds 3 liters, which is 3000 ml

    # Calculate the total volume of water that can be collected in the pot
    total_volume = pot_capacity

    # Calculate the volume of water collected per minute
    volume_per_minute = drops_per_minute * volume_per_drop

    # Calculate the time it will take for the pot to be full
    time_to_fill = total_volume / volume_per_minute

    result = time_to_fill
    return result

print(solution())