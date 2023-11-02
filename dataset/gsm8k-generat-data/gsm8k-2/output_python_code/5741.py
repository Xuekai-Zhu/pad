def solution():
    """Jazel has 3 sticks. One stick is 3 centimeters long. The second stick is twice as long while the third stick is 1 centimeter shorter than the second stick. What is the total length of Jazel's sticks when they are put together?"""
    first_stick = 3
    second_stick = 2 * first_stick
    third_stick = second_stick - 1
    total_length = first_stick + second_stick + third_stick
    result = total_length
    return result

print(solution())