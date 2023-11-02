def solution():
    """Joey needs to take a new prescription. The first day he needs to take one pill. Each day he must take two more pills than the previous day. How many pills will he take in a week?"""
    # Define the number of pills Joey takes on the first day
    first_day_pills = 1

    # Calculate the total number of pills Joey takes in a week (7 days)
    total_pills = sum(range(first_day_pills, first_day_pills + 7*2, 2))

    # Return the result
    result = total_pills
    return result

print(solution())