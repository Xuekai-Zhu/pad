def solution():
    # Define the size of the class
    class_size = 45

    # Calculate the size of each age group
    under_11 = class_size / 3
    above_11_below_13 = (2 / 5) * class_size

    # Calculate the size of the third age group
    third_group = class_size - under_11 - above_11_below_13

    result = third_group
    return result

print(solution())