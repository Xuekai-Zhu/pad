def solution():
    # Calculate the length of the second stick and the third stick
    second_stick = 2 * 3  # the second stick is twice as long as the first stick
    third_stick = second_stick - 1  # the third stick is 1 centimeter shorter than the second stick

    # Calculate the total length of Jazel's sticks
    total_length = 3 + second_stick + third_stick
    result = total_length
    return result

print(solution())