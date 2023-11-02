def solution():
    packets_per_day = 2  # Christopher uses 2 packets of sugar substitute per day
    packets_per_box = 30  # Each box contains 30 packets of sugar substitute
    cost_per_box = 4.00  # Each box costs $4.00
    days = 90  # Christopher wants to have enough sugar substitute for 90 days

    # Calculate the total number of packets Christopher needs for 90 days
    total_packets = packets_per_day * days

    # Calculate the total number of boxes Christopher needs to buy
    total_boxes = total_packets / packets_per_box

    # Calculate the total cost of buying enough sugar substitute for 90 days
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())