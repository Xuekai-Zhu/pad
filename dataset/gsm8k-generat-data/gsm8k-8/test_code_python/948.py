def solution():
    # Define William's number of visits per week
    william_visits_per_week = 2

    # Calculate Jason's number of visits per week
    jason_visits_per_week = 4 * william_visits_per_week

    # Calculate Jason's total number of visits in 4 weeks
    jason_total_visits = jason_visits_per_week * 4

    result = jason_total_visits
    return result

print(solution())