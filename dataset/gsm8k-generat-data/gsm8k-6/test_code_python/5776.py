def solution():
    # Calculate the number of sunscreen bottles needed
    num_applications = 16 // 2  # she needs to re-apply every 2 hours, so there are 8 applications in 16 hours
    num_bottles = num_applications // 4 + 1  # each bottle has 4 applications and she needs to round up to make sure she has enough
    total_cost = num_bottles * 3.5  # each bottle costs $3.5

    result = total_cost
    return result

print(solution())