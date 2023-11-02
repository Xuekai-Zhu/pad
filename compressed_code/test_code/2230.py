def solution():
    
    peaches_per_basket = 25
    num_baskets = 5
    total_peaches = peaches_per_basket * num_baskets
    eaten_peaches = 5
    remaining_peaches = total_peaches - eaten_peaches
    boxes_of_peaches = remaining_peaches // 15
    result = boxes_of_peaches
    return result

print(solution())