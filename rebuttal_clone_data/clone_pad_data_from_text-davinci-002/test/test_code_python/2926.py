def solution():
    base_price = 10.00
    topping_1 = 2.00
    toppings_2_3 = 1.00
    toppings_4_on = 0.50
    total_toppings = topping_1 + (toppings_2_3 * 2) + (toppings_4_on * 5)
    slice_price = (base_price + total_toppings) / 8
    result = slice_price
    
    return result

print(solution())