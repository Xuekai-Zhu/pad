def solution():
    bottles_per_day = 0.5
    days_supply = 240
    bottles_per_case = 24
    cases_needed = days_supply / bottles_per_case
    cost_per_case = 12
    total_cost = cases_needed * cost_per_case
    result = total_cost
    return result

print(solution())