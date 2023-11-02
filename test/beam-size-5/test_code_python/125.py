def solution():
    
    people_per_day = 500
    minutes_per_patient = 24
    patients_per_day = people_per_day * minutes_per_patient
    cost_per_patient = 150
    cost_per_hour = 200
    total_cost = (patients_per_day * cost_per_patient) + (patients_per_day * cost_per_hour)
    profit = total_cost - total_cost
    result = profit
    return result

print(solution())