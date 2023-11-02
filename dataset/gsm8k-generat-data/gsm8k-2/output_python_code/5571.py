def solution():
    """Alicia had a wonderful birthday party where she got lots of presents. 10 of the presents were in small boxes. 12 of the presents were in medium boxes. A third of all the presents she is given are in large boxes. How many presents did Alicia get for her birthday?"""
    small_boxes = 10
    medium_boxes = 12
    large_boxes = (small_boxes + medium_boxes) / 3
    total_presents = small_boxes + medium_boxes + large_boxes
    result = total_presents
    return result

print(solution())