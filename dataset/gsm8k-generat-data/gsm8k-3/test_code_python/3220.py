def solution():
    """Tom takes medication to help him sleep.  He takes 2 pills every day before bed.  He needs to go to the doctor every 6 months to get a new prescription and a visit to the doctor costs $400.  The medication costs $5 per pill, but insurance covers 80% of that cost.  How much does he pay a year for everything?"""
    # Define the cost of each pill and the insurance coverage
    PILL_COST = 5
    INSURANCE_COVERAGE = 0.8

    # Define the number of pills Tom takes per day and per year
    pills_per_day = 2
    pills_per_year = pills_per_day * 365

    # Calculate the annual cost of the medication
    medication_cost = pills_per_year * PILL_COST * (1 - INSURANCE_COVERAGE)

    # Define the cost of each doctor visit and the number of visits per year
    DOCTOR_VISIT_COST = 400
    visits_per_year = 2

    # Calculate the annual cost of the doctor visits
    doctor_visit_cost = visits_per_year * DOCTOR_VISIT_COST

    # Calculate the total annual cost
    total_cost = medication_cost + doctor_visit_cost

    # Display the total annual cost
    result = total_cost
    return result

print(solution())