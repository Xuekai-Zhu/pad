def solution():
    # Calculate the cost for visiting the museum once a month for one year at $5 per visit
    cost_per_month = 5
    visits_per_year = 12
    total_cost_year_1 = cost_per_month * visits_per_year

    # Calculate the cost for visiting the museum 4 times a year at $7 per visit for the next two years
    cost_per_visit_year_2_and_3 = 7
    visits_per_year_year_2_and_3 = 4
    total_cost_year_2_and_3 = cost_per_visit_year_2_and_3 * visits_per_year_year_2_and_3 * 2

    # Calculate the total cost for all visits after 3 years
    total_cost = total_cost_year_1 + total_cost_year_2_and_3
    result = total_cost
    return result

print(solution())