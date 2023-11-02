def solution():
    # Calculate the number of ounces Cassie needs to drink per day
    ounces_per_day = 12 * 8
    
    # Calculate the number of times Cassie needs to refill her water bottle
    refills_per_day = ounces_per_day / 16
    
    result = refills_per_day
    return result

print(solution())