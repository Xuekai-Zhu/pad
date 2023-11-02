def solution():
    """In a classroom, there are blue chairs, green chairs, and white chairs. There are 10 blue chairs. The green chairs are 3 times as many as the blue chairs, and there are 13 fewer white chairs than the green and blue chairs combined. How many chairs are there in a classroom?"""
    blue_chairs = 10
    green_chairs = 3 * blue_chairs
    total_blue_green_chairs = blue_chairs + green_chairs
    white_chairs = total_blue_green_chairs - 13
    total_chairs = blue_chairs + green_chairs + white_chairs
    result = total_chairs
    return result

print(solution())