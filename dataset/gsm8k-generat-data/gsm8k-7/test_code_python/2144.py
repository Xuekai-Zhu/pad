def solution():
    num_days = 40
    num_cups_per_day = 3
    num_pods_per_cup = 1
    pods_per_box = 30
    cost_per_box = 8.0

    # Calculate the total number of coffee pods that Sharon will use
    total_pods = num_days * num_cups_per_day * num_pods_per_cup

    # Calculate the total number of boxes of coffee pods that Sharon will need to buy
    total_boxes = (total_pods // pods_per_box) + 1 # Round up to the nearest whole box

    # Calculate the total cost of all boxes of coffee pods that Sharon will buy
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())