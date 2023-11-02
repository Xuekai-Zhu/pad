def solution():
    # Calculate how much Gwen spent on each stock
    bonus = 900
    stock_a = bonus / 3
    stock_b = bonus / 3
    stock_c = bonus / 3

    # Calculate the new values of each stock after one year
    stock_a_value = stock_a * 2
    stock_b_value = stock_b * 2
    stock_c_value = stock_c * 0.5

    # Calculate the total value of all three stocks
    total_value = stock_a_value + stock_b_value + stock_c_value

    result = total_value
    return result

print(solution())