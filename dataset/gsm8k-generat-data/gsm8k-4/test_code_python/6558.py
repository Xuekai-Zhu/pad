def solution():
    """It takes 20 minutes for John to go to the bathroom 8 times. How long would it take to go 6 times?"""
    # Define the time and frequency variables
    time = 20
    freq = 8

    # Calculate the time per bathroom break
    time_per_break = time / freq

    # Calculate the time for 6 bathroom breaks
    total_time = time_per_break * 6

    # Return the result
    result = total_time
    return result

print(solution())