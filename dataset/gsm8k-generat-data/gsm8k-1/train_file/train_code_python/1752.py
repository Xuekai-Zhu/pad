def solution():
    """Christopher uses 1 packet of a sugar substitute in his coffee. He has 2 coffees a day. The packets come 30 to a box and cost $4.00 a box. How much will it cost him to have enough sugar substitutes to last him 90 days?"""
    packets_per_day = 2
    packets_per_box = 30
    days_per_box = packets_per_box / packets_per_day
    boxes_needed = 90 / days_per_box
    cost_per_box = 4
    total_cost = boxes_needed * cost_per_box

    result = total_cost
    return result

print(solution())