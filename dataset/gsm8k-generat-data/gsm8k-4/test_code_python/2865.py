def solution():
    """There were 25 peaches in each basket. Five baskets of peaches were delivered to a market. 
    The farmers have eaten 5 peaches. The remaining peaches are packed into smaller boxes of 15 each. 
    How many boxes of peaches are there?"""
    # Define the number of peaches in each basket and the number of baskets delivered
    peaches_per_basket = 25
    baskets_delivered = 5

    # Calculate the total number of peaches delivered
    total_peaches = peaches_per_basket * baskets_delivered

    # Subtract the number of peaches eaten by the farmers
    total_peaches -= 5

    # Calculate the number of boxes needed to pack the remaining peaches
    boxes_needed = total_peaches // 15

    # If there are any remaining peaches, add another box
    if total_peaches % 15 != 0:
        boxes_needed += 1

    # Return the result
    result = boxes_needed
    return result

print(solution())