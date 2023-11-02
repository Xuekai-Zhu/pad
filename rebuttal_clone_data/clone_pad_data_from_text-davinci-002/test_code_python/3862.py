def solution():
    adult_patients_per_hour = 4
    child_patients_per_hour = 3
    cost_per_adult_visit = 50
    cost_per_child_visit = 25
    hours_worked = 8
    
    total_adult_patients = adult_patients_per_hour * hours_worked
    total_child_patients = child_patients_per_hour * hours_worked
    
    total_revenue = (total_adult_patients * cost_per_adult_visit) + (total_child_patients * cost_per_child_visit)
    
    result = total_revenue
    
    return result

print(solution())