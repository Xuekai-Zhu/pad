def solution():
    packets_per_day = 2
    packets_per_box = 30
    cost_per_box = 4.00

    total_days = 90
    total_packets_needed = packets_per_day * total_days
    total_boxes_needed = (total_packets_needed - 1) // packets_per_box + 1
    total_cost = total_boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())