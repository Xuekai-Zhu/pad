def solution():
    """A farmer gets 20 pounds of bacon on average from a pig. He sells each pound for $6 at the monthly farmer’s market. This month’s pig is a runt that grew to only half the size of the average pig. How many dollars will the farmer make from the pig’s bacon?"""
    average_bacon = 20
    runt_bacon = average_bacon / 2
    price_per_pound = 6
    total_price = runt_bacon * price_per_pound
    result = total_price
    return result

print(solution())