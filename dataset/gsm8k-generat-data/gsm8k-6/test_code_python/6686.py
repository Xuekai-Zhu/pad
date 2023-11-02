def solution():
    # Calculate the number of servings of champagne needed
    servings_needed = 2 * 120  # each guest receives 2 glasses of champagne

    # Calculate the number of bottles of champagne needed
    bottles_needed = servings_needed / 6  # each bottle has 6 servings

    result = bottles_needed
    return result

print(solution())