def solution():
    water_cooler = 3 * 128  # The water cooler initially contains 3 gallons of water, with 128 ounces in each gallon
    dixie_cup = 6  # Each Dixie cup holds 6 ounces of water
    total_cups = 5 * 10  # There are 5 rows of chairs and 10 chairs in each row, so there are 50 chairs in total

    # Calculate the total amount of water used to fill all the cups
    total_water_used = total_cups * dixie_cup

    # Calculate the amount of water left in the cooler
    water_left = water_cooler - total_water_used
    result = water_left
    return result

print(solution())