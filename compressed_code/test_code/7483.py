def solution():
    
    days = 40
    coffee_per_day = 3
    pods_per_coffee = 1
    pods_per_box = 30
    cost_per_box = 8.00
    total_coffee_pods = days * coffee_per_day * pods_per_coffee
    total_boxes_needed = total_coffee_pods / pods_per_box
    total_cost = total_boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())