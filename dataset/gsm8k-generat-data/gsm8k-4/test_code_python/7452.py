def solution():
    """Gwen received a $900 bonus at work and decided to invest this money in the stock market. She spent one-third of her bonus on stock A, one-third on stock B, and the remaining one-third on stock C. After one year, stock A and stock B had doubled in value, while stock C had lost half of its value. At the end of the year, how much were Gwen's stocks worth, in dollars?"""
    # Define the initial investment and the amount spent on each stock
    initial_investment = 900
    stock_a_investment = initial_investment / 3
    stock_b_investment = initial_investment / 3
    stock_c_investment = initial_investment / 3

    # Calculate the value of stock A after one year
    stock_a_value = stock_a_investment * 2

    # Calculate the value of stock B after one year
    stock_b_value = stock_b_investment * 2

    # Calculate the value of stock C after one year
    stock_c_value = stock_c_investment * 0.5

    # Calculate the total value of all three stocks after one year
    total_value = stock_a_value + stock_b_value + stock_c_value

    # Return the result
    result = total_value
    return result

print(solution())