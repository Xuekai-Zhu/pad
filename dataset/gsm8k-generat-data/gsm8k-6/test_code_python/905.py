def solution():
    # Calculate the number of cans of soda produced by one machine in 8 hours
    cans_per_hour = 2 * 30  # the machine produces 30 cans of soda every 30 minutes, so it produces 60 cans per hour
    total_cans = cans_per_hour * 8  # multiply by the number of hours
    result = total_cans
    return result

print(solution())