def solution():
    """Jazel has 3 sticks. One stick is 3 centimeters long. The second stick is twice as long while the third stick is 1 centimeter shorter than the second stick. What is the total length of Jazel's sticks when they are put together?"""
    # Define the length of the first stick
    stick1 = 3

    # Calculate the length of the second stick
    stick2 = 2 * stick1

    # Calculate the length of the third stick
    stick3 = stick2 - 1

    # Calculate the total length of Jazel's sticks
    total_length = stick1 + stick2 + stick3

    result = total_length
    return result

print(solution())