def solution():
    
    peach_price = 2
    apple_price = 1
    blueberry_price = 1
    pies = [5, 4, 3]
    fruit_per_pie = 3
    peach_total = pies[0] * fruit_per_pie * peach_price
    apple_total = pies[1] * fruit_per_pie * apple_price
    blueberry_total = pies[2] * fruit_per_pie * blueberry_price
    total_cost = peach_total + apple_total + blueberry_total
    result = total_cost
    return result

print(solution())