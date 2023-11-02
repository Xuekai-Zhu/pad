def solution():
    vaccines_cost = 10 * 45  # The cost of 10 vaccines, each costing $45
    doctor_visit_cost = 250  # The cost of the doctor's visit, $250
    total_medical_cost = vaccines_cost + doctor_visit_cost  # The total cost of the medical expenses
    insurance_coverage = 0.8  # The insurance will cover 80% of the medical expenses
    covered_medical_cost = total_medical_cost * insurance_coverage  # The amount of medical expenses covered by insurance
    uncovered_medical_cost = total_medical_cost - covered_medical_cost  # The amount of medical expenses not covered by insurance
    total_trip_cost = 1200  # The cost of the trip itself
    total_cost = uncovered_medical_cost + total_trip_cost  # The total cost of the trip, including medical expenses not covered by insurance
    result = total_cost
    return result

print(solution())