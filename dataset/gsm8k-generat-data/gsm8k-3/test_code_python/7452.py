def solution():
    """Gwen received a $900 bonus at work and decided to invest this money in the stock market.  She spent one-third of her bonus on stock A, one-third on stock B, and the remaining one-third on stock C.   After one year, stock A and stock B had doubled in value, while stock C had lost half of its value.  At the end of the year, how much were Gwen's stocks worth, in dollars?"""
    # Define the initial bonus amount and the fraction of it spent on each stock
    bonus = 900
    fraction = 1/3
    
    # Calculate the amount spent on each stock
    a_amount = fraction * bonus
    b_amount = fraction * bonus
    c_amount = fraction * bonus
    
    # Calculate the value of each stock after one year
    a_value = a_amount * 2
    b_value = b_amount * 2
    c_value = c_amount * 0.5
    
    # Calculate the total value of all stocks
    total_value = a_value + b_value + c_value

    # Display the total value of all stocks
    result = total_value
    return result

print(solution())