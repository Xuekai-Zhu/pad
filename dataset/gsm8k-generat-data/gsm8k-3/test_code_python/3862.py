def solution():
    """When Doctor Lindsay works in her office, she usually sees 4 adult patients and 3 child patients every hour. If the cost for an adult's office visit is $50, and the cost for a child's office visit is $25, how much money, in dollars, does Doctor Lyndsay receive in a typical 8-hour day for seeing all her patients?"""
    # Define the number of adult and child patients per hour
    ADULT_PATIENTS = 4
    CHILD_PATIENTS = 3

    # Define the cost of an adult and child's office visit
    ADULT_COST = 50
    CHILD_COST = 25

    # Calculate the number of adult and child patients per day
    total_patients = (ADULT_PATIENTS + CHILD_PATIENTS) * 8

    # Calculate the total cost of all adult and child visits
    total_cost = (ADULT_PATIENTS * ADULT_COST + CHILD_PATIENTS * CHILD_COST) * 8

    # Display the total cost
    result = total_cost
    return result

print(solution())