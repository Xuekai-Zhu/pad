def solution():
    peaches_per_basket = 25
    baskets_delivered = 5
    peaches_eaten = 5
    peaches_remaining = peaches_per_basket * baskets_delivered - peaches_eaten
    peaches_per_box = 15
    boxes_of_peaches = peaches_remaining / peaches_per_box
    result = boxes_of_peaches
    return result

print(solution())