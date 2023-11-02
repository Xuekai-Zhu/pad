def solution():
    # Calculate the total volume of water in the glasses
    total_volume = 10 * 6 * 4/5

    # Calculate the total volume of water needed to fill the glasses to the brim
    total_volume_needed = 10 * 6

    # Calculate the additional amount of water needed
    additional_volume = total_volume_needed - total_volume
    result = additional_volume
    return result

print(solution())