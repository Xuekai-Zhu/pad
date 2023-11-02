def solution():
    
    vaccine_cost = 10 * 45
    doctor_visit_cost = 250
    insurance_coverage = 0.8
    total_medical_cost = (vaccine_cost + doctor_visit_cost) * (1 - insurance_coverage)
    trip_cost = 1200
    total_cost = total_medical_cost + trip_cost
    result = total_cost
    return result

print(solution())