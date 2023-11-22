def solution():
    
    # Define the number of visits Pauline visits
    visits_per_year = 3

    # Define the cost of one visit
    visit_cost = 2

    # Calculate the total cost of all visits for the first 5 years
    total_visit_cost_5_years = visit_cost * visits_per_year * 5

    # Calculate the cost of one visit after 5 years
    visit_cost_after_5_years = visit_cost * 1.5

    # Calculate the total cost of all visits for the next 3 years
    total_visit_cost_3_years = visit_cost_after_5_years * visits_per_year * 3

    # Calculate the total cost of all visits
    total_cost = total_visit_cost_5_years + total_visit_cost_3_years

    # Display the total cost
    result = total_cost
    return result

print(solution())