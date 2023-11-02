def solution():
    
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