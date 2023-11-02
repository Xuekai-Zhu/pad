def solution():
    """Jazel has 3 sticks. One stick is 3 centimeters long. The second stick is twice as long while the third stick is 1 centimeter shorter than the second stick. What is the total length of Jazel's sticks when they are put together?"""
    stick1 = 3
    stick2 = stick1 * 2
    stick3 = stick2 - 1
    total_length = stick1 + stick2 + stick3
    result = total_length
    return result

print(solution())