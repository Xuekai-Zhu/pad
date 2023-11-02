def solution():
    """John invests in a bank and gets 10% simple interest.  He invests $1000.  How much money does he have after 3 years?"""
    # Define the initial investment and the interest rate
    initial_investment = 1000
    interest_rate = 0.1

    # Calculate the interest earned after 3 years
    interest_earned = initial_investment * interest_rate * 3

    # Calculate the total amount of money John has after 3 years
    total_money = initial_investment + interest_earned

    # Display the total amount of money John has after 3 years
    result = total_money
    return result

print(solution())