def solution():
    """Josh built his little brother a rectangular sandbox. The perimeter of the sandbox is 30 feet and the length is twice the width. What is the width of the sandbox?"""
    perimeter = 30
    length = 0
    width = 0
    for i in range(1, perimeter):
        width = i
        length = 2 * width
        if 2 * length + 2 * width == perimeter:
            break
    result = width
    return result

print(solution())