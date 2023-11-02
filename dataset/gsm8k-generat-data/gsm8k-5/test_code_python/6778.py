def solution():
    first_day = 1  # Joey needs to take one pill on the first day
    pills_per_day = 2  # Joey has to take two more pills than the previous day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of pills Joey will take in a week
    total_pills = first_day
    for i in range(2, days_per_week + 1):
        total_pills += first_day + ((i - 1) * pills_per_day)
    result = total_pills
    return result

print(solution())