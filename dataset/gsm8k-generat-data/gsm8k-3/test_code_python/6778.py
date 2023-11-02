def solution():
    """Joey needs to take a new prescription. The first day he needs to take one pill. Each day he must take two more pills than the previous day. How many pills will he take in a week?"""
    # Define the number of pills Joey takes on the first day and the number of days in a week
    first_day = 1
    days_in_week = 7

    # Calculate the total number of pills Joey takes in a week
    total_pills = first_day
    for i in range(2, days_in_week+1):
        total_pills += first_day + (i-1)*2

    # Display the total number of pills Joey takes in a week
    result = total_pills
    return result

print(solution())