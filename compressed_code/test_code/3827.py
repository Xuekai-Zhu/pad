def solution():
    
    tinsel_per_box = 4
    christmas_tree_per_box = 1
    snow_globes_per_box = 5
    decorations_per_box = tinsel_per_box + christmas_tree_per_box + snow_globes_per_box
    total_boxes = 11 + 1
    total_decorations = decorations_per_box * total_boxes
    result = total_decorations
    return result

print(solution())