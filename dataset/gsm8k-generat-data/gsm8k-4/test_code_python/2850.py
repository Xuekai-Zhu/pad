def solution():
    """Mr. John works at a shopping mall and receives a monthly income of $2000, but he spends approximately 5% of this amount on public transport to and from the mall in a month. How much will he have left after deducting his monthly transport fare from his income?"""
    # Define Mr. John's monthly income
    monthly_income = 2000

    # Calculate the amount spent on transport
    transport_cost = monthly_income * 0.05

    # Calculate the amount left after deducting transport cost
    amount_left = monthly_income - transport_cost

    # return the result
    result = amount_left
    return result

print(solution())