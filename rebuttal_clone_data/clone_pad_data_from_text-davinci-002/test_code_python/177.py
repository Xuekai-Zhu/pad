def solution():
 """James decides to replace his car. He sold his $20,000 car for 80% of its value and then was able to haggle to buy a $30,000 sticker price car for 90% of its value. How much was he out of pocket?"""
    
    old_car_value = 20000
    old_car_sale_price = old_car_value * 0.8
    new_car_list_price = 30000
    new_car_sale_price = new_car_list_price * 0.9
    total_cost = new_car_sale_price - old_car_sale_price
    result = total_cost
    return result

print(solution())