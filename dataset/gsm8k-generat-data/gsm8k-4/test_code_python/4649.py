def solution():
    """A machine fills 150 cans of paint every 8 minutes. How many minutes does it take this machine to fill 675 cans?"""
    # Define the number of cans filled in 1 minute
    cans_per_minute = 150 / 8

    # Calculate the number of minutes it takes to fill 675 cans
    minutes = 675 / cans_per_minute

    # Return the result
    result = minutes
    return result

print(solution())