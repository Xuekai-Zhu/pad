def solution():
    # Define the number of levels of the pyramid
    num_levels = 4

    # Define the number of cases needed for each level of the pyramid
    cases_per_level = []
    for i in range(1, num_levels + 1):
        cases_per_level.append(i ** 2)

    # Calculate the total number of cases needed
    total_cases = sum(cases_per_level)

    result = total_cases
    return result

print(solution())