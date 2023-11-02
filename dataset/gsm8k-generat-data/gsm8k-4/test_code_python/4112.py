def solution():
    """A farmer gets 20 pounds of bacon on average from a pig. He sells each pound for $6 at the monthly farmer’s market. This month’s pig is a runt that grew to only half the size of the average pig. How many dollars will the farmer make from the pig’s bacon?"""
    # Define the average bacon yield and the price per pound
    AVG_BACON_YIELD = 20
    PRICE_PER_POUND = 6

    # Calculate the bacon yield for the runt pig
    runt_bacon_yield = AVG_BACON_YIELD / 2

    # Calculate the total revenue from selling the bacon
    total_revenue = runt_bacon_yield * PRICE_PER_POUND

    # return the result
    result = total_revenue
    return result

print(solution())