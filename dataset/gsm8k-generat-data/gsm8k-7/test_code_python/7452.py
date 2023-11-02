def solution():
    bonus = 900

    # Calculate how much Gwen invested in each stock
    stock_a = bonus / 3
    stock_b = bonus / 3
    stock_c = bonus / 3

    # Calculate the value of stock A after one year
    stock_a_value = stock_a * 2

    # Calculate the value of stock B after one year
    stock_b_value = stock_b * 2

    # Calculate the value of stock C after one year
    stock_c_value = stock_c * 0.5

    # Calculate the total value of all stocks after one year
    total_value = stock_a_value + stock_b_value + stock_c_value
    result = total_value
    return result

print(solution())