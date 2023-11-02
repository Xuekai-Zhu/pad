def solution():
    pills_per_day = 2  # Tom takes 2 pills every day
    cost_per_pill = 5  # The medication costs $5 per pill
    insurance_coverage = 0.8  # Insurance covers 80% of the medication cost
    pills_per_year = pills_per_day * 365  # Tom takes pills every day for a year
    medication_cost_per_year = pills_per_year * cost_per_pill * (1 - insurance_coverage)  # Calculate the cost of medication for a year
    doctor_visit_cost = 400  # A doctor visit costs $400
    visits_per_year = 2  # Tom visits the doctor twice a year
    total_cost_per_year = medication_cost_per_year + (doctor_visit_cost * visits_per_year)  # Calculate the total cost per year
    result = total_cost_per_year
    return result

print(solution())