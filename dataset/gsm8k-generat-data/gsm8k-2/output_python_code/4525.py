def solution():
    """Tom wants to visit Barbados. He needs to get 10 different vaccines to go and a doctor's visit. They each cost $45 and the doctor's visit costs $250 but insurance will cover 80% of these medical bills. The trip itself cost $1200. How much will he have to pay?"""
    vaccine_cost = 10 * 45
    doctor_visit_cost = 250
    insurance_coverage = 0.8
    total_medical_cost = (vaccine_cost + doctor_visit_cost) * (1 - insurance_coverage)
    trip_cost = 1200
    total_cost = total_medical_cost + trip_cost
    result = total_cost
    return result

print(solution())