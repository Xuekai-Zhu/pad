def solution():
    """A farmer gets 20 pounds of bacon on average from a pig. He sells each pound for $6 at the monthly farmer’s market. This month’s pig is a runt that grew to only half the size of the average pig. How many dollars will the farmer make from the pig’s bacon?"""
    # Define the average weight of a pig and the price per pound
    AVG_WEIGHT = 20
    PRICE_PER_POUND = 6

    # Calculate the weight of the runt pig and the total revenue from its bacon
    runt_weight = AVG_WEIGHT / 2
    revenue = runt_weight * PRICE_PER_POUND

    # Display the total revenue
    result = revenue
    return result

print(solution())