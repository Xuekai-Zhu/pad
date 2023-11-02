def solution():
    # Calculate the total number of bread and baguette baked in 6 hours
    bread_baked = (10 * 6) + (30 * (6 // 2)) # (10 loaves per hour * 6 hours) + (30 baguettes per 2 hours * 3 sets of 2 hours in 6 hours)
    result = bread_baked
    return result

print(solution())