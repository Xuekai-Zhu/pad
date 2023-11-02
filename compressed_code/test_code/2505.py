def solution():
    
    pills_per_day = 2
    pills_per_year = pills_per_day * 365
    medication_cost_per_pill = 5 * 0.2 
    doctor_visit_cost = 400
    visits_per_year = 2 
    total_medication_cost = medication_cost_per_pill * pills_per_year
    total_doctor_visits_cost = doctor_visit_cost * visits_per_year
    total_cost = total_medication_cost + total_doctor_visits_cost
    result = total_cost
    return result

print(solution())