def solution():
    """Justin has a box that is 12 inches in height. The length of the box is 3 times its height and 4 times its width. What is the volume of the box?"""
    # Define the height of the box
    height = 12

    # Calculate the length and width of the box
    length = height * 3
    width = length / 4

    # Calculate the volume of the box
    volume = height * length * width

    # Return the result
    result = volume
    return result

print(solution())