def solution():
    # Calculate the cost of medication for one day
    pills_per_day = 2
    cost_per_pill = 5 * 0.8
    cost_per_day = pills_per_day * cost_per_pill

    # Calculate the cost of medication for one year
    days_per_year = 365
    cost_per_year = days_per_year * cost_per_day

    # Calculate the cost of doctor visits for one year
    visits_per_year = 2
    cost_per_visit = 400
    cost_of_visits_per_year = visits_per_year * cost_per_visit

    # Calculate the total cost for one year
    total_cost = cost_per_year + cost_of_visits_per_year
    result = total_cost
    return result

print(solution())