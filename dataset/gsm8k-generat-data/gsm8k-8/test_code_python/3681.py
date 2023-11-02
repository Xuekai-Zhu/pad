def solution():
    # Calculate the volume of the pot in milliliters
    pot_volume = 3000

    # Calculate the volume of one drop in milliliters
    drop_volume = 20

    # Calculate the total drops needed to fill the pot
    total_drops = pot_volume / drop_volume

    # Calculate the time it will take to fill the pot in minutes
    time_to_fill = total_drops / 3
    result = time_to_fill
    return result

print(solution())