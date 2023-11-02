def solution():
    """Tom takes medication to help him sleep. He takes 2 pills every day before bed. He needs to go to the doctor every 6 months to get a new prescription and a visit to the doctor costs $400. The medication costs $5 per pill, but insurance covers 80% of that cost. How much does he pay a year for everything?"""
    pills_per_day = 2
    doctor_visits_per_year = 2
    doctor_visit_cost = 400
    pill_cost = 5
    insurance_coverage = 0.8
    pills_per_year = pills_per_day * 365
    pills_cost_per_year = pills_per_year * pill_cost * (1 - insurance_coverage)
    doctor_visit_cost_per_year = doctor_visits_per_year * doctor_visit_cost
    total_cost = pills_cost_per_year + doctor_visit_cost_per_year
    result = total_cost
    return result

print(solution())