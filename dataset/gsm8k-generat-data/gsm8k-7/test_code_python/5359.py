def solution():
    cups_per_day = 12
    ounces_per_cup = 8
    ounces_per_bottle = 16

    # Calculate the total number of ounces of water Cassie needs to drink per day
    total_ounces_per_day = cups_per_day * ounces_per_cup

    # Calculate the number of times Cassie needs to refill her water bottle per day
    num_refills_per_day = total_ounces_per_day / ounces_per_bottle
    result = num_refills_per_day
    return result

print(solution())