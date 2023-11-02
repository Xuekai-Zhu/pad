def solution():
    total_donuts = 10 * 12
    donuts_left = total_donuts - 12 - 8
    boxes = donuts_left // 10
    result = boxes
    return result

print(solution())