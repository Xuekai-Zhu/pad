def solution():
    """Lisa and Peter are selling chocolate bars door to door. Lisa sold three and a half boxes of chocolate bars, and Peter sold four and a half boxes. They sold 64 chocolate bars together. How many chocolate bars are in a box?"""
    lisa_boxes = 3.5
    peter_boxes = 4.5
    total_boxes = lisa_boxes + peter_boxes
    total_bars = 64
    bars_per_box = total_bars / total_boxes
    result = bars_per_box
    return result

print(solution())