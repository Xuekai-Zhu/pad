def solution():
    """Tom wants to visit Barbados. He needs to get 10 different vaccines to go and a doctor's visit. They each cost $45 and the doctor's visit costs $250 but insurance will cover 80% of these medical bills. The trip itself cost $1200. How much will he have to pay?"""
    vaccine_cost = 10 * 45
    doctor_visit_cost = 250
    insurance_coverage = 0.8
    medical_bills = vaccine_cost + doctor_visit_cost
    covered_bills = medical_bills * insurance_coverage
    uncovered_bills = medical_bills - covered_bills
    total_cost = uncovered_bills + covered_bills + 1200
    result = total_cost
    return result

print(solution())