def solution():
    pull_ups_per_visit = 2  # Mike does 2 pull-ups each time he enters his office
    visits_per_day = 5  # Mike visits his office 5 times per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total number of pull-ups Mike does in a week
    total_pull_ups = pull_ups_per_visit * visits_per_day * days_per_week
    result = total_pull_ups
    return result

print(solution())