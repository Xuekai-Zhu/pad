def solution():
    num_pills_per_day = 2
    pill_cost = 5
    insurance_coverage = 0.8
    num_doctor_visits_per_year = 2
    doctor_visit_cost = 400
    num_days_in_six_months = 6 * 30

    # Calculate the total cost of pills for one year
    pills_per_year = num_pills_per_day * 365
    total_pill_cost_per_year = pills_per_year * pill_cost * (1 - insurance_coverage)

    # Calculate the total cost of doctor visits for one year
    total_doctor_visit_cost_per_year = num_doctor_visits_per_year * doctor_visit_cost

    # Calculate the total cost of everything for one year
    total_cost_per_year = total_pill_cost_per_year + total_doctor_visit_cost_per_year
    result = total_cost_per_year
    return result

print(solution())