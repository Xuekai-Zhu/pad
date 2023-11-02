def solution():
    
    total_donuts = 10 * 12
    jeff_donuts = total_donuts - 12
    chris_donuts = 8
    remaining_donuts = jeff_donuts - chris_donuts
    boxes = remaining_donuts // 10
    result = boxes
    return result

print(solution())