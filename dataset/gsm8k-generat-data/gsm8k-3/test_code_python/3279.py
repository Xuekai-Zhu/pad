def solution():
    """Four kids can wash three whiteboards in 20 minutes. How long would it take, in minutes, for one kid to wash six whiteboards?"""
    # Define the constant values
    KIDS = 4
    WHITEBOARDS = 3

    # Calculate the total number of whiteboards washed per minute
    whiteboards_per_minute = (KIDS * WHITEBOARDS) / 20

    # Calculate the time it would take for one kid to wash six whiteboards
    time = 6 / whiteboards_per_minute

    # Display the time
    result = time
    return result

print(solution())