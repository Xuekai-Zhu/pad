def solution():
    """It took Dad 5 more than twice as long to vacuum upstairs then to vacuum downstairs. He vacuumed for a total of 38 minutes. How many minutes did he vacuum upstairs?"""
    # Let x be the time in minutes to vacuum downstairs
    # Then 2x+5 is the time in minutes to vacuum upstairs
    # The total vacuuming time is 38 minutes

    # Set up the equation
    x = (38 - 5) / 3
    upstairs_time = 2 * x + 5

    # Return the result
    result = upstairs_time
    return result

print(solution())