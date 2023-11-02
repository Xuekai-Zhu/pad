def solution():
    """Christopher uses 1 packet of a sugar substitute in his coffee. He has 2 coffees a day. 
    The packets come 30 to a box and cost $4.00 a box. How much will it cost him to have enough sugar substitutes to last him 90 days?"""
    # Calculate the number of packets Christopher needs per day
    packets_per_day = 2 * 1

    # Calculate the total number of packets Christopher needs for 90 days
    packets_90_days = packets_per_day * 90

    # Calculate the number of boxes Christopher needs
    boxes = packets_90_days / 30

    # Calculate the total cost of the boxes
    cost = boxes * 4

    # Return the result
    result = cost
    return result

print(solution())