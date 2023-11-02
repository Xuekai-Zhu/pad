def solution():
    
    peach_pies = 5
    apple_pies = 4
    blueberry_pies = 3
    pounds_of_fruit_per_pie = 3
    peach_price_per_pound = 2
    apple_price_per_pound = 1
    blueberry_price_per_pound = 1
    total_cost = (peach_pies * pounds_of_fruit_per_pie * peach_price_per_pound) + (apple_pies * pounds_of_fruit_per_pie * apple_price_per_pound) + (blueberry_pies * pounds_of_fruit_per_pie * blueberry_price_per_pound)
    result = total_cost
    return result

print(solution())