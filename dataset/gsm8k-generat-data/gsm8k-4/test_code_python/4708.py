def solution():
    """Mirasol had $50 in her account. She spent $10 on coffee beans and $30 on a tumbler. How much is left in her account?"""
    starting_balance = 50
    coffee_cost = 10
    tumbler_cost = 30

    # Calculate the remaining balance after the coffee and tumbler purchases
    remaining_balance = starting_balance - coffee_cost - tumbler_cost

    # Return the remaining balance
    result = remaining_balance
    return result

print(solution())