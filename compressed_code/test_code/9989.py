def solution():
    
    peach_price = 0.4
    num_peaches = 400
    peach_cost = peach_price * num_peaches
    discount = (peach_cost // 10) * 2
    total_cost = peach_cost - discount
    result = total_cost
    return result

print(solution())