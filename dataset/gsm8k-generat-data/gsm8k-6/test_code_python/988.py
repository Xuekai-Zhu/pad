def solution():
    height = 12  # height of the box in inches
    length = 3 * height  # length of the box is 3 times its height
    width = height/4  # width of the box is 1/4th its height
    volume = height * length * width  # formula for volume of a box
    result = volume
    return result

print(solution())