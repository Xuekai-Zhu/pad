def solution():
    
    lisa_boxes = 3.5
    peter_boxes = 4.5
    total_boxes = 64
    lisa_bars = lisa_boxes * 3
    peter_bars = peter_boxes * 4
    total_bars = lisa_bars + peter_bars
    bars_per_box = total_bars / total_boxes
    result = bars_per_box
    return result

print(solution())