def solution():
    """Justin has a box that is 12 inches in height. The length of the box is 3 times its height and 4 times its width. What is the volume of the box?"""
    # Define the height of the box
    height = 12

    # Calculate the length of the box
    length = 3 * height

    # Calculate the width of the box
    width = length / 4

    # Calculate the volume of the box
    volume = length * width * height

    # Display the volume of the box
    result = volume
    return result

print(solution())