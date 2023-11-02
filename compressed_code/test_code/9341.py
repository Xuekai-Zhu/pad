def solution():
    
    slippers_count = 6
    lipstick_count = 4
    hair_color_count = 8
    
    slippers_price = 2.5
    lipstick_price = 1.25
    hair_color_price = 3
    
    slippers_cost = slippers_count * slippers_price
    lipstick_cost = lipstick_count * lipstick_price
    hair_color_cost = hair_color_count * hair_color_price
    
    total_cost = slippers_cost + lipstick_cost + hair_color_cost
    result = total_cost
    
    return result

print(solution())