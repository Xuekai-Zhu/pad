def solution():
    """Hawkeye is driving to his aunt. He has to charge his battery for $3.5 per charge. If he charged his battery four times, and his battery charging budget was $20, how much money was he left with when he reached his aunt's place?"""
    # Define the cost per charge
    CHARGE_COST = 3.5

    # Define the number of charges Hawkeye needs
    num_charges = 4

    # Define Hawkeye's charging budget
    charging_budget = 20

    # Calculate the total cost of charging Hawkeye's battery
    total_cost = CHARGE_COST * num_charges

    # Calculate the amount of money Hawkeye has left after charging his battery
    money_left = charging_budget - total_cost

    # Display the amount of money Hawkeye has left
    result = money_left
    return result

print(solution())