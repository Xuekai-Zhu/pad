def solution():
    # Calculate the number of cans of chickpeas needed for 20 servings of hummus
    ounces_per_can = 16
    ounces_per_serving = 6
    cups_per_serving = ounces_per_serving / 8  # convert ounces to cups
    cans_needed = 20 * cups_per_serving / (ounces_per_can / 8)  # convert ounces to cups and divide by ounces per can
    result = cans_needed
    return result

print(solution())