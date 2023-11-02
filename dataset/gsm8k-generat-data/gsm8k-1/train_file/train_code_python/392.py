def solution():
    """Josh built his little brother a rectangular sandbox. The perimeter of the sandbox is 30 feet and the length is twice the width. What is the width of the sandbox?"""
    perimeter = 30
    length = 0
    width = 0
    for i in range(1, perimeter//2):
        if (perimeter - 2 * i) % 2 == 0 and i * ((perimeter - 2 * i) // 2) > length:
            length = i * ((perimeter - 2 * i) // 2)
            width = (perimeter - 2 * i) // 2
    result = width
    return result

print(solution())