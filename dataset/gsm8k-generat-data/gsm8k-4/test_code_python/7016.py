def solution():
    """At its current growth rate, a certain plant will be 80 feet tall after a year. If the plant grows at the same rate every month and is currently 20 feet tall, what's its monthly growth rate in feet?"""
    # Define the initial height and the final height
    initial_height = 20
    final_height = 80

    # Calculate the total growth over the year
    total_growth = final_height - initial_height

    # Calculate the monthly growth rate
    monthly_growth = total_growth / 12

    # Return the result
    result = monthly_growth
    return result

print(solution())