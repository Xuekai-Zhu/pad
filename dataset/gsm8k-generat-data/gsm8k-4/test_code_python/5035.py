def solution():
    """An investment bank gives 10 percent interest at the end of every month. How much money in total will you have, including interest, at the end of 2 months if you invest $300?"""
    # Define the initial investment, the monthly interest rate, and the number of months
    initial_investment = 300
    monthly_interest_rate = 0.1
    num_months = 2

    # Calculate the total amount of money after the specified number of months, including interest
    total_amount = initial_investment
    for i in range(num_months):
        total_amount *= (1 + monthly_interest_rate)

    # Round the result to 2 decimal places
    result = round(total_amount, 2)
    return result

print(solution())