def solution():
    
    boxes = 4
    decorations_per_box = 15
    total_decorations = boxes * decorations_per_box
    decorations_used = 35
    decorations_given = total_decorations - decorations_used
    result = decorations_given
    return result

print(solution())