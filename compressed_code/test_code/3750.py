def solution():
    
    lemon_price = 2
    papaya_price = 1
    mango_price = 4
    total_fruits = 6 + 4 + 2
    total_cost = (6 * lemon_price) + (4 * papaya_price) + (2 * mango_price)
    discount = (total_fruits // 4) * 1
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())