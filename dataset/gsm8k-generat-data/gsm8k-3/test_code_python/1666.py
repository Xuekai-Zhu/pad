def solution():
    """Calvin buys a pack of chips, for $0.50, from the vending machine at lunch, 5 days a week. After 4 weeks, how much money has Calvin spent on chips?"""
    # Define the cost of chips
    COST_PER_PACK = 0.5

    # Define the number of days per week Calvin buys chips
    DAYS_PER_WEEK = 5

    # Define the number of weeks
    NUM_WEEKS = 4

    # Calculate the total cost of chips over 4 weeks
    total_cost = COST_PER_PACK * DAYS_PER_WEEK * NUM_WEEKS

    # Display the total cost
    result = total_cost
    return result

print(solution())