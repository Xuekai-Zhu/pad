def solution():
    """Free Christmas decorations are being given out to families. Each box of decorations contains 4 pieces of tinsel, 1 Christmas tree and 5 snow globes. If 11 families receive a box of decorations and another box is given to the community center, how many decorations have been handed out?"""
    tinsel_per_box = 4
    christmas_tree_per_box = 1
    snow_globes_per_box = 5
    decorations_per_box = tinsel_per_box + christmas_tree_per_box + snow_globes_per_box
    total_boxes = 11 + 1
    total_decorations = decorations_per_box * total_boxes
    result = total_decorations
    return result

print(solution())