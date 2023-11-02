def solution():
    """The news announced a $0.4 oil price rollback this Friday. Mr. Deane decided to only fill his gas tank with 10 liters of gas today and then another 25 liters on Friday. If the cost per liter of gas is $1.4 today, how much will Mr. Deane spend for his 35 liters of gas?"""
    # Define the initial cost per liter of gas and the rollback amount
    INITIAL_COST = 1.4
    ROLLBACK_AMOUNT = 0.4

    # Define the number of liters of gas to be purchased
    liters_total = 35
    liters_today = 10
    liters_friday = 25

    # Calculate the cost of gas purchased today
    cost_today = liters_today * INITIAL_COST

    # Calculate the cost of gas purchased on Friday after the rollback
    cost_friday = liters_friday * (INITIAL_COST - ROLLBACK_AMOUNT)

    # Calculate the total cost of gas purchased
    total_cost = cost_today + cost_friday

    # Return the result
    result = round(total_cost, 2)
    return result

print(solution())