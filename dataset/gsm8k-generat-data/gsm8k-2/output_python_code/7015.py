def solution():
    """At its current growth rate, a certain plant will be 80 feet tall after a year. If the plant grows at the same rate every month and is currently 20 feet tall, what's its monthly growth rate in feet?"""
    total_growth = 80 - 20  # total growth needed in feet
    months = 12  # number of months in a year
    monthly_growth = total_growth / months
    result = monthly_growth
    return result

print(solution())