def solution():
    # Calculate the number of ounces of chickpeas needed for 20 servings
    chickpeas_needed = 20 * 6

    # Calculate the number of cans of chickpeas needed, rounding up to the nearest whole number
    cans_needed = math.ceil(chickpeas_needed / 16)
    result = cans_needed
    return result

print(solution())