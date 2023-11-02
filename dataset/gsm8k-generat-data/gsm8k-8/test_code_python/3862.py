def solution():
    # Define the number of patients per hour
    adult_patients_per_hour = 4
    child_patients_per_hour = 3

    # Define the cost per visit
    adult_visit_cost = 50
    child_visit_cost = 25

    # Calculate the total revenue for one hour
    total_revenue_per_hour = adult_patients_per_hour * adult_visit_cost + child_patients_per_hour * child_visit_cost

    # Calculate the total revenue for the entire day
    total_revenue_per_day = total_revenue_per_hour * 8

    result = total_revenue_per_day
    return result

print(solution())