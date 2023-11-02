def solution():
    
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