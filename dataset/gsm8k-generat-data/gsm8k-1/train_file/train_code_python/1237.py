def solution():
    """There are 3 boxes of cereal. One box holds 14 ounces of cereal. Another box holds half the amount of the first box and 5 ounces less than the third box. How much cereal is there in all 3 cereal boxes?"""
    box1 = 14
    box2 = box1 / 2
    box3 = box2 + 5
    total_cereal = box1 + box2 + box3
    result = total_cereal
    return result

print(solution())