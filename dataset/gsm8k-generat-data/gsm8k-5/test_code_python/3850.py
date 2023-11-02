def solution():
    total_cases = 0  # Initialize the total number of cases

    # Calculate the number of cases for each level and add them up
    for i in range(1, 5):
        level_cases = i ** 2  # Calculate the number of cases for this level
        total_cases += level_cases  # Add the number of cases for this level to the total

    result = total_cases
    return result

print(solution())