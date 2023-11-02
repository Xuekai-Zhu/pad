def solution():
    """Tom takes medication to help him sleep. He takes 2 pills every day before bed. He needs to go to the doctor every 6 months to get a new prescription and a visit to the doctor costs $400. The medication costs $5 per pill, but insurance covers 80% of that cost. How much does he pay a year for everything?"""
    pills_per_day = 2
    pills_per_year = pills_per_day * 365
    medication_cost_per_pill = 5 * 0.2 # after insurance
    doctor_visit_cost = 400
    visits_per_year = 2 # every 6 months
    total_medication_cost = medication_cost_per_pill * pills_per_year
    total_doctor_visits_cost = doctor_visit_cost * visits_per_year
    total_cost = total_medication_cost + total_doctor_visits_cost
    result = total_cost
    return result

print(solution())