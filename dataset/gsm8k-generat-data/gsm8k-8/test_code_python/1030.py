def solution():
    # Calculate the total number of chairs
    total_chairs = 5 * 10

    # Calculate the total number of cups needed
    cups_needed = total_chairs

    # Calculate the total amount of water in ounces
    total_water = 3 * 128

    # Calculate the amount of water used in filling the cups
    cups_filled = cups_needed * 6
    water_used = cups_filled

    # Calculate the amount of water left in the cooler
    water_left = total_water - water_used
    result = water_left
    return result

print(solution())