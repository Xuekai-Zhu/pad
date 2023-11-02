def solution():
    # Calculate the total number of Dixie cups needed
    total_cups = 5 * 10  # 5 rows with 10 chairs in each row

    # Calculate the total volume of water in ounces needed for all cups
    total_volume = 6 * total_cups

    # Calculate the total volume of water in gallons
    total_volume_gallons = total_volume / 128

    # Calculate the amount of water left in the cooler
    water_left = 3 - total_volume_gallons

    # Convert the amount of water left to ounces
    water_left_ounces = water_left * 128

    result = water_left_ounces
    return result

print(solution())