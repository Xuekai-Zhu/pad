def solution():
    """Jazel has 3 sticks. One stick is 3 centimeters long. The second stick is twice as long while the third stick is 1 centimeter shorter than the second stick. What is the total length of Jazel's sticks when they are put together?"""
    # Define the length of the first stick
    stick1_length = 3

    # Define the length of the second stick
    stick2_length = 2 * stick1_length

    # Define the length of the third stick
    stick3_length = stick2_length - 1

    # Calculate the total length of the sticks
    total_length = stick1_length + stick2_length + stick3_length

    # Display the total length
    result = total_length
    return result

print(solution())