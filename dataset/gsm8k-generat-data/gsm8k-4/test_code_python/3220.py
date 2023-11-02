def solution():
    """Tom takes medication to help him sleep. He takes 2 pills every day before bed. He needs to go to the doctor every 6 months to get a new prescription and a visit to the doctor costs $400. The medication costs $5 per pill, but insurance covers 80% of that cost. How much does he pay a year for everything?"""
    # Define the cost of a single pill and the number of pills Tom takes daily
    pill_cost = 5
    pills_per_day = 2

    # Calculate the yearly cost of the medication with insurance coverage
    yearly_medication_cost = pill_cost * pills_per_day * 365 * 0.2

    # Calculate the yearly cost of doctor visits
    yearly_doctor_cost = 2 * 400

    # Calculate the total yearly cost
    total_cost = yearly_medication_cost + yearly_doctor_cost

    result = total_cost
    return result

print(solution())