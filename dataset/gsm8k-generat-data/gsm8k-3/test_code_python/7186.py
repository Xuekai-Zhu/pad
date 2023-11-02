def solution():
    """During a commercial break in the Super Bowl, there were three 5-minute commercials and eleven 2-minute commercials. How many minutes was the commercial break?"""
    # Define the length of each type of commercial
    long_commercial_length = 5
    short_commercial_length = 2

    # Define the number of each type of commercial
    num_long_commercials = 3
    num_short_commercials = 11

    # Calculate the total length of the commercial break
    total_length = (long_commercial_length * num_long_commercials) + (short_commercial_length * num_short_commercials)

    # Display the total length of the commercial break
    result = total_length
    return result

print(solution())