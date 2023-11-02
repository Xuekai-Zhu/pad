def solution():
    
    lychees_harvested = 500
    lychees_sold = lychees_harvested / 2
    lychees_remaining = lychees_harvested - lychees_sold
    lychees_consumed = (3/5) * lychees_remaining
    lychees_remaining_after_consumption = lychees_remaining - lychees_consumed
    result = lychees_remaining_after_consumption
    return result

print(solution())