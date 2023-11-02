def solution():
    
    initial_green_apples = 32
    initial_red_apples = initial_green_apples + 200
    green_apples_after_delivery = initial_green_apples + 340
    red_apples_after_delivery = initial_red_apples
    difference = green_apples_after_delivery - red_apples_after_delivery
    result = difference
    
    return result

print(solution())