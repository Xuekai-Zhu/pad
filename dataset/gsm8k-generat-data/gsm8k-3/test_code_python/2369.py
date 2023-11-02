def solution():
    """Jason has a carriage house that he rents out.  He’s charging $50.00 per day or $500.00 for 14 days.  Eric wants to rent the house for 20 days.  How much will it cost him?"""
    # Define the cost per day and the cost for 14 days
    COST_PER_DAY = 50
    COST_FOR_14_DAYS = 500

    # Determine if Eric will rent for more than 14 days
    if 20 <= 14:
        # Eric will pay $50 per day
        total_cost = 20 * COST_PER_DAY
    else:
        # Eric will pay $500 for the first 14 days and $50 per day for any additional days
        additional_days = 20 - 14
        total_cost = COST_FOR_14_DAYS + additional_days * COST_PER_DAY

    # Display the total cost for Eric
    result = total_cost
    return result

print(solution())