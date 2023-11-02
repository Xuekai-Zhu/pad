def solution():
    # Calculate the number of packets needed for 90 days
    packets_needed = 1 * 2 * 90  # 1 packet per coffee, 2 coffees per day, 90 days

    # Calculate the number of boxes needed
    boxes_needed = packets_needed // 30 + 1  # rounding up to the nearest box

    # Calculate the total cost
    total_cost = boxes_needed * 4.00

    result = total_cost
    return result

print(solution())