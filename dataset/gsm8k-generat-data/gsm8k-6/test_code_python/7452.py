def solution():
    total_bonus = 900  # Gwen received a $900 bonus
    stock_A = total_bonus/3  # Gwen spent one-third of her bonus on stock A
    stock_B = total_bonus/3  # Gwen spent one-third of her bonus on stock B
    stock_C = total_bonus/3  # Gwen spent one-third of her bonus on stock C
    stock_A_new = stock_A * 2  # Stock A doubled in value
    stock_B_new = stock_B * 2  # Stock B doubled in value
    stock_C_new = stock_C * 0.5  # Stock C lost half of its value
    total_value = stock_A_new + stock_B_new + stock_C_new  # Total worth of Gwen's stocks after one year

    result = total_value
    return result

print(solution())