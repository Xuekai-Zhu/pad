def solution():
    
    coffee_price = 6
    cheesecake_price = 10
    discount_percent = 25
    total_price = coffee_price + cheesecake_price
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount
    result = final_price
    return result

print(solution())