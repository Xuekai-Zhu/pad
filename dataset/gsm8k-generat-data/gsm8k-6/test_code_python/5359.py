def solution():
    # Calculate the number of times Cassie needs to refill her water bottle
    cups_per_day = 12
    ounces_per_cup = 8
    ounces_per_bottle = 16
    refill_times = cups_per_day * ounces_per_cup / ounces_per_bottle
    result = refill_times
    return result

print(solution())