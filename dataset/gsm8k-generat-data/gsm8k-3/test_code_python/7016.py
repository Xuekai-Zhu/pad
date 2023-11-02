def solution():
    """At its current growth rate, a certain plant will be 80 feet tall after a year. If the plant grows at the same rate every month and is currently 20 feet tall, what's its monthly growth rate in feet?"""
    # Define the current height, target height, and time period in months
    current_height = 20
    target_height = 80
    time_period = 12

    # Calculate the monthly growth rate required to reach the target height
    growth_rate = (target_height - current_height) / time_period

    # Display the monthly growth rate
    result = growth_rate
    return result

print(solution())