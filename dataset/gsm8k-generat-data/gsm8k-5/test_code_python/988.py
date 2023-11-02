def solution():
    height = 12  # Height of the box is 12 inches
    length = 3 * height  # Length of the box is 3 times its height
    width = length / 4  # Width of the box is 1/4th of its length

    # Calculate the volume of the box
    volume = height * length * width
    result = volume
    return result

print(solution())