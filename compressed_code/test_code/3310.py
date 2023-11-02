def solution():
    
    regular_price = 15
    discount_percentage = 40
    discount = regular_price * discount_percentage / 100
    final_price = regular_price - discount
    result = final_price
    return result

print(solution())