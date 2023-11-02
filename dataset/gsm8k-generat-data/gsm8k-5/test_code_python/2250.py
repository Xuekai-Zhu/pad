def solution():
    servings_per_cup = 1  # One serving of hummus requires 1 cup of chickpeas
    ounces_per_can = 16  # One can of chickpeas contains 16 ounces of chickpeas
    ounces_per_cup = 6  # One cup of chickpeas contains 6 ounces of chickpeas
    servings_to_make = 20  # Thomas wants to make 20 servings

    # Calculate the total cups of chickpeas needed
    cups_needed = servings_to_make * servings_per_cup

    # Calculate the total ounces of chickpeas needed
    ounces_needed = cups_needed * ounces_per_cup

    # Calculate the total number of cans of chickpeas needed (rounded up to the nearest whole can)
    cans_needed = math.ceil(ounces_needed / ounces_per_can)

    result = cans_needed
    return result

print(solution())