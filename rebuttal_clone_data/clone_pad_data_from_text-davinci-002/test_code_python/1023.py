def solution():
    length = 20
    width = 5
    height = 2
    bricks_needed = (2 * length * height) + (2 * width * height) + (length * width)
    result = bricks_needed
    return result

print(solution())