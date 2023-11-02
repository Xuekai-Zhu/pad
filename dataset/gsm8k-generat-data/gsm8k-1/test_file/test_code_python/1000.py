def solution():
    """Peter has 4 boxes with the same number of chocolate bars in each, while Martha has 7 boxes with the same number of chocolate bars in each. If Peter and Martha have totals of 64 and 56 chocolate bars respectively, how many more chocolate bars does Peter have in each box than Martha?"""
    peter_boxes = 4
    martha_boxes = 7
    peter_bars = 64
    martha_bars = 56
    peter_bars_per_box = peter_bars / peter_boxes
    martha_bars_per_box = martha_bars / martha_boxes
    difference = peter_bars_per_box - martha_bars_per_box
    result = difference
    return result

print(solution())