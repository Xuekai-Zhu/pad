def solution():
    """Justin has a box that is 12 inches in height. The length of the box is 3 times its height and 4 times its width. What is the volume of the box?"""
    height = 12
    length = 3 * height
    width = length / 4
    volume = height * length * width
    result = volume
    return result

print(solution())