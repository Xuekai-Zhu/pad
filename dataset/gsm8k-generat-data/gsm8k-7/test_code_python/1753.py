def solution():
    packets_per_day = 2
    packets_per_box = 30
    cost_per_box = 4.0
    num_days = 90

    # Calculate the total number of packets that Christopher needs for 90 days
    total_packets = packets_per_day * num_days

    # Calculate the total number of boxes that Christopher needs to buy
    total_boxes = total_packets / packets_per_box

    # Calculate the total cost of all boxes of sugar substitute that Christopher needs to buy
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())