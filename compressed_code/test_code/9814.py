def solution():
    
    curtis_meal_price = 16.00
    rob_meal_price = 18.00
    discount_percent = 50
    total_meal_price = curtis_meal_price + rob_meal_price
    discounted_meal_price = total_meal_price * (discount_percent / 100)
    final_bill = discounted_meal_price
    return final_bill

print(solution())