def solution():
    """Christopher uses 1 packet of a sugar substitute in his coffee.  He has 2 coffees a day.  The packets come 30 to a box and cost $4.00 a box.  How much will it cost him to have enough sugar substitutes to last him 90 days?"""
    # Define the number of packets Christopher uses each day
    packets_per_day = 2

    # Calculate the number of packets Christopher will need for 90 days
    packets_needed = packets_per_day * 90

    # Calculate the number of boxes Christopher will need to buy
    boxes_needed = packets_needed / 30
    boxes_needed = math.ceil(boxes_needed)  # round up to the nearest whole box

    # Calculate the total cost of the sugar substitutes
    total_cost = boxes_needed * 4.00

    # Display the total cost
    result = total_cost
    return result

print(solution())