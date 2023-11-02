def solution():
    butter_needed = 2 * 6  # The recipe calls for 2 ounces of butter for every 1 cup of baking mix, so for 6 cups, 12 ounces of butter is needed
    butter_remaining = 4  # The chef has 4 ounces of butter remaining

    # If the chef can only use as much butter as possible, he will need to use 8 ounces of coconut oil to substitute for the remaining 8 ounces of butter
    if butter_remaining >= butter_needed:
        coconut_oil_needed = 0
    else:
        coconut_oil_needed = butter_needed - butter_remaining

    result = coconut_oil_needed
    return result

print(solution())