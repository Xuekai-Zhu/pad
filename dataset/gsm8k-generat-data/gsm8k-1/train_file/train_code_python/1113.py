def solution():
    """Jeff makes 10 donuts each day for 12 days. Jeff eats one of the donuts each day. Chris then comes over and eats 8 donuts. If 10 donuts fit in each box, how many boxes can Jeff fill with his donuts?"""
    total_donuts = 10 * 12
    donuts_left = total_donuts - 12 - 8
    donuts_per_box = 10
    boxes_filled = donuts_left // donuts_per_box
    result = boxes_filled
    return result

print(solution())