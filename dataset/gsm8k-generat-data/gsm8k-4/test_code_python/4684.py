def solution():
    """In the second hour of a storm it rains 7 inches more than twice the amount it rained the first hour. The total amount of rain in the first two hours is 22 inches. How much did it rain in the first hour?"""
    # Define the amount of rain in the first hour as x
    x = None

    # Calculate the amount of rain in the second hour
    y = 2*x + 7

    # Calculate the total amount of rain in the first two hours
    total_rain = x + y

    # Use the total amount of rain to solve for x
    x = (22 - y) / 2

    # Round x to 1 decimal place
    result = round(x, 1)
    return result

print(solution())