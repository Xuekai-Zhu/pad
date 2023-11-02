def solution():
    # Calculate the total number of weeks spent on the island
    first_expedition = 3
    second_expedition = first_expedition + 2
    last_expedition = 2 * second_expedition
    total_weeks = first_expedition + second_expedition + last_expedition

    # Convert total weeks to days
    total_days = total_weeks * 7
    result = total_days
    return result

print(solution())