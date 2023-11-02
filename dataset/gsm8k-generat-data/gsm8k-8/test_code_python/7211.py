def solution():
    # Define variables
    total_inches = 40 * 12
    daily_strip = 6 * 12
    nightly_growth = 2 * 12
    days = 0

    # Loop until all ivy is stripped off
    while total_inches > 0:
        total_inches -= daily_strip
        total_inches += nightly_growth
        days += 1

    result = days
    return result

print(solution())