def solution():
    # Define the ratio of sugar to water
    sugar_to_water_ratio = 1 : 2

    # Calculate the total number of cups of sugar needed for one liter of lemonade
    cups_of_sugar_per_liter = sugar_to_water_ratio[0] / sum(sugar_to_water_ratio)

    # Calculate the total number of liters of lemonade made with 84 cups of sugar
    total_liters = 84 / cups_of_sugar_per_liter

    # Calculate the total number of cups of sugar used
    total_cups_of_sugar = total_liters * sugar_to_water_ratio[0]
    result = total_cups_of_sugar
    return result

print(solution())