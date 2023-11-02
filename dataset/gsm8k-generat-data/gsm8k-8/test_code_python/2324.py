def solution():
    # Define the variables
    hourly_rate = 5
    hours_per_day = 5
    afternoons_per_week = 6
    weeks = 7

    # Calculate the total number of hours babysat
    total_hours = hours_per_day * afternoons_per_week * weeks

    # Calculate the total amount earned
    total_earned = total_hours * hourly_rate

    result = total_earned
    return result

print(solution())