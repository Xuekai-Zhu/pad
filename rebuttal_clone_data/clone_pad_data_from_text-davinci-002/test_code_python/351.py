def solution():
    number_of_weeks = 36
    sandwiches_per_week = 2
    number_of_missed_days = 3
    total_number_of_sandwiches = (number_of_weeks * sandwiches_per_week) - number_of_missed_days
    result = total_number_of_sandwiches
    return result

print(solution())