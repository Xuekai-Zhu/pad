def solution():
    """At its current growth rate, a certain plant will be 80 feet tall after a year. If the plant grows at the same rate every month and is currently 20 feet tall, what's its monthly growth rate in feet?"""
    height_initial = 20
    height_final = 80
    time_months = 12
    growth_rate = (height_final - height_initial) / time_months
    result = growth_rate
    return result

print(solution())