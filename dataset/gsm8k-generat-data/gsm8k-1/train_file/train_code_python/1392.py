def solution():
    """Cassy packs 12 jars of jam in 10 boxes while she packs 10 jars of jam in 30 boxes. If she has 500 jars of jams, how many jars of jam will she have left when all the boxes are full?"""
    jars_per_box1 = 12
    boxes1 = 10
    jars_per_box2 = 10
    boxes2 = 30
    total_boxes = (500 // jars_per_box1 + 500 // jars_per_box2) // (boxes1 + boxes2)
    remaining_jars = 500 - (total_boxes * (boxes1 * jars_per_box1 + boxes2 * jars_per_box2))
    result = remaining_jars
    return result

print(solution())