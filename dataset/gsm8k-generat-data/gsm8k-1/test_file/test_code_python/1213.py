def solution():
    """Pauline visits her favorite local museum three times a year. The cost of one visit is $2. After 5 years, the cost of one visit has increased by 150%, but Pauline decided not to give up any visit and continued to go to the museum for 3 more years. How much did Pauline spend on all visits to the museum?"""
    visits_per_year = 3
    cost_per_visit = 2
    years_before_increase = 5
    percent_increase = 150
    years_after_increase = 3
    
    # Calculate cost before increase
    total_visits_before_increase = visits_per_year * years_before_increase
    cost_before_increase = total_visits_before_increase * cost_per_visit
    
    # Calculate cost after increase
    cost_per_visit_after_increase = cost_per_visit * (1 + percent_increase/100)
    total_visits_after_increase = visits_per_year * years_after_increase
    cost_after_increase = total_visits_after_increase * cost_per_visit_after_increase
    
    # Calculate total cost
    total_cost = cost_before_increase + cost_after_increase
    
    result = total_cost
    return result

print(solution())