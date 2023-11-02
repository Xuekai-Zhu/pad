def solution():
    # Calculate the cost of medication for one year
    pills_per_day = 2
    pills_per_year = pills_per_day * 365
    cost_per_pill = 5 * 0.2  # 80% of the cost is covered by insurance
    medication_cost_per_year = pills_per_year * cost_per_pill

    # Calculate the cost of doctor visits for one year
    visits_per_year = 2  # Tom visits the doctor every 6 months
    doctor_visit_cost_per_year = visits_per_year * 400

    # Calculate the total cost for one year
    total_cost_per_year = medication_cost_per_year + doctor_visit_cost_per_year
    result = total_cost_per_year
    return result

print(solution())