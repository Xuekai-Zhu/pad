def solution():
    peaches_per_basket = 25
    num_baskets = 5
    num_peaches_eaten = 5
    peaches_left = (peaches_per_basket * num_baskets) - num_peaches_eaten
    peaches_per_box = 15
    num_boxes = peaches_left // peaches_per_box
    if peaches_left % peaches_per_box != 0:
        num_boxes += 1
    result = num_boxes
    return result

print(solution())