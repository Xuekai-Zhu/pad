def solution():
    """There were 25 peaches in each basket. Five baskets of peaches were delivered to a market. The farmers have eaten 5 peaches. The remaining peaches are packed into smaller boxes of 15 each. How many boxes of peaches are there?"""
    # Define the number of peaches per basket and the number of baskets delivered
    PEACHES_PER_BASKET = 25
    BASKETS_DELIVERED = 5

    # Calculate the total number of peaches delivered
    total_peaches = PEACHES_PER_BASKET * BASKETS_DELIVERED

    # Subtract the number of peaches the farmers ate
    remaining_peaches = total_peaches - 5

    # Calculate the number of boxes of 15 peaches that can be packed
    boxes = remaining_peaches // 15

    # Display the number of boxes
    result = boxes
    return result

print(solution())