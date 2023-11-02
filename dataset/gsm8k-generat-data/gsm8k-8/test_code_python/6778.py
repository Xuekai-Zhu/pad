def solution():
    # Define the number of days in a week and the starting number of pills
    days_in_week = 7
    starting_pills = 1

    # Calculate the total number of pills Joey will take in a week
    total_pills = starting_pills
    for day in range(2, days_in_week + 1):
        total_pills += starting_pills + 2 * (day - 1)

    result = total_pills
    return result

print(solution())