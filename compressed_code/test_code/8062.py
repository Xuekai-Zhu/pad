def solution():
    
    peaches_per_basket = 25
    baskets_delivered = 5
    peaches_eaten = 5
    remaining_peaches = peaches_per_basket * baskets_delivered - peaches_eaten
    boxes_packed = remaining_peaches // 15
    result = boxes_packed
    return result

print(solution())