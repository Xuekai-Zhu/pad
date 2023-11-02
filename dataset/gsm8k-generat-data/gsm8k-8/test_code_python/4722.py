def solution():
    # Calculate the number of dresses Jane sews in the first 7 days
    first_week_dresses = 2 * 7

    # Calculate the number of dresses Jane sews in the next 2 days
    next_two_days_dresses = 3 * 2

    # Calculate the total number of dresses Jane sews
    total_dresses = first_week_dresses + next_two_days_dresses

    # Calculate the total number of ribbons Jane uses
    total_ribbons = total_dresses * 2

    result = total_ribbons
    return result

print(solution())