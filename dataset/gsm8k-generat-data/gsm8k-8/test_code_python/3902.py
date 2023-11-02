def solution():
    # Calculate how many ounces of butter are needed for 6 cups of baking mix
    butter_needed = 6 * 2

    # Determine how much butter can be used before switching to coconut oil
    if butter_needed <= 4:
        butter_used = butter_needed
        coconut_oil_used = 0
    else:
        butter_used = 4
        coconut_oil_used = butter_needed - butter_used

    result = coconut_oil_used
    return result

print(solution())