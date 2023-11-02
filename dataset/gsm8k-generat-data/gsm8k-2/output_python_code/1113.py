def solution():
    """Jeff makes 10 donuts each day for 12 days. Jeff eats one of the donuts each day. Chris then comes over and eats 8 donuts. If 10 donuts fit in each box, how many boxes can Jeff fill with his donuts?"""
    total_donuts = 10 * 12
    jeff_donuts = total_donuts - 12
    chris_donuts = 8
    remaining_donuts = jeff_donuts - chris_donuts
    boxes = remaining_donuts // 10
    result = boxes
    return result

print(solution())