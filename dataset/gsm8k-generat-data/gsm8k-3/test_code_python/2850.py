def solution():
    """Mr. John works at a shopping mall and receives a monthly income of $2000, but he spends approximately 5% of this amount on public transport to and from the mall in a month. How much will he have left after deducting his monthly transport fare from his income?"""
    # Define John's monthly income
    monthly_income = 2000

    # Calculate the amount John spends on transport
    transport_cost = monthly_income * 0.05

    # Calculate John's income after deducting transport cost
    net_income = monthly_income - transport_cost

    # Display John's net income
    result = net_income
    return result

print(solution())