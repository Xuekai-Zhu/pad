def solution():
    
    hotdog_price = 1.5
    salad_price = 2.5
    num_hotdogs = 5
    num_salads = 3
    total_cost = (hotdog_price * num_hotdogs) + (salad_price * num_salads)
    paid_amount = 10 * 2
    change = paid_amount - total_cost
    result = change
    return result

print(solution())