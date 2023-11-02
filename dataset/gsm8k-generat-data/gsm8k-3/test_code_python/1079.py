def solution():
    """Mr. Roberts can buy a television for $400 cash or $120 down payment and $30 a month for 12 months. How much can he save by paying cash?"""
    # Calculate the cost of buying the television with monthly payments
    monthly_cost = 120 + 30 * 12

    # Calculate the savings if buying with cash
    savings = monthly_cost - 400

    # Display the savings
    result = savings
    return result

print(solution())