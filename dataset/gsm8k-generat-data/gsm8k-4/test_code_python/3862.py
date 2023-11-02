def solution():
    """When Doctor Lindsay works in her office, she usually sees 4 adult patients and 3 child patients every hour. If the cost for an adult's office visit is $50, and the cost for a child's office visit is $25, how much money, in dollars, does Doctor Lyndsay receive in a typical 8-hour day for seeing all her patients?"""
    # Define the number of adult and child patients per hour and the cost per visit
    ADULT_PATIENTS_PER_HOUR = 4
    CHILD_PATIENTS_PER_HOUR = 3
    ADULT_COST_PER_VISIT = 50
    CHILD_COST_PER_VISIT = 25

    # Calculate the total number of patients seen in 8 hours
    total_adult_patients = ADULT_PATIENTS_PER_HOUR * 8
    total_child_patients = CHILD_PATIENTS_PER_HOUR * 8
    total_patients = total_adult_patients + total_child_patients

    # Calculate the total amount of money earned for seeing all patients
    total_earned = (total_adult_patients * ADULT_COST_PER_VISIT) + (total_child_patients * CHILD_COST_PER_VISIT)

    # Return the result
    result = total_earned
    return result

print(solution())