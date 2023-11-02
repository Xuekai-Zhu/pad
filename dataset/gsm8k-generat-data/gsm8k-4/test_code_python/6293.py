def solution():
    """John invests in a bank and gets 10% simple interest. He invests $1000. How much money does he have after 3 years?"""
    # Define the initial investment and interest rate
    initial_investment = 1000
    interest_rate = 0.1

    # Calculate the interest earned and total amount after 3 years
    interest_earned = initial_investment * interest_rate * 3
    total_amount = initial_investment + interest_earned

    # Return the result
    result = total_amount
    return result

print(solution())