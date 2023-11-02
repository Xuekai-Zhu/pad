def solution():
    # Calculate the total number of drops in 2 hours
    total_time = 2 * 60  # convert hours to minutes
    total_drops = total_time * 20

    # Calculate the total amount of liquid in milliliters
    total_liquid = (total_drops / 100) * 5

    result = total_liquid
    return result

print(solution())