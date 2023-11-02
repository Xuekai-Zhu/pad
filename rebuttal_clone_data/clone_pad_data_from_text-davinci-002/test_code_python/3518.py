def solution():
    length = 12
    width = 16
    height = 10
    area = length * width + (2 * length * height) + (2 * width * height)
    time = area / 40
    result = time
    return result

print(solution())