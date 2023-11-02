def solution():
    """Calvin buys a pack of chips, for $0.50, from the vending machine at lunch, 5 days a week. After 4 weeks, how much money has Calvin spent on chips?"""
    # Define the cost of one pack of chips and the number of days per week
    CHIP_COST = 0.5
    DAYS_PER_WEEK = 5

    # Calculate the total cost of chips for one week
    weekly_cost = CHIP_COST * DAYS_PER_WEEK

    # Calculate the total cost of chips for four weeks
    total_cost = weekly_cost * 4

    # Display the total cost of chips
    result = total_cost
    return result

print(solution())