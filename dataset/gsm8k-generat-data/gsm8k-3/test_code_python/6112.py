def solution():
    """Tim gets a manicure and tips the beautician 30%.  If the manicure cost $30 how much did he pay in total?"""
    # Define the cost of the manicure
    MANICURE_COST = 30

    # Calculate the tip amount
    tip_amount = MANICURE_COST * 0.3

    # Calculate the total cost
    total_cost = MANICURE_COST + tip_amount

    # Display the total cost
    result = total_cost
    return result

print(solution())