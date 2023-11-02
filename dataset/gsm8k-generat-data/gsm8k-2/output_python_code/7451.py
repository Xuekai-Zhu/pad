def solution():
    """Gwen received a $900 bonus at work and decided to invest this money in the stock market. She spent one-third of her bonus on stock A, one-third on stock B, and the remaining one-third on stock C. After one year, stock A and stock B had doubled in value, while stock C had lost half of its value. At the end of the year, how much were Gwen's stocks worth, in dollars?"""
    bonus = 900
    stock_a = bonus / 3
    stock_b = bonus / 3
    stock_c = bonus - stock_a - stock_b

    stock_a_value = stock_a * 2
    stock_b_value = stock_b * 2
    stock_c_value = stock_c * 0.5

    total_value = stock_a_value + stock_b_value + stock_c_value
    result = total_value
    return result

print(solution())