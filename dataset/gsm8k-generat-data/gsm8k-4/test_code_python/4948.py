def solution():
    """Free Christmas decorations are being given out to families. Each box of decorations contains 4 pieces of tinsel, 1 Christmas tree and 5 snow globes. If 11 families receive a box of decorations and another box is given to the community center, how many decorations have been handed out?"""
    # Define the number of decorations in each box
    tinsel_per_box = 4
    tree_per_box = 1
    snowglobe_per_box = 5

    # Calculate the total number of boxes
    total_boxes = 11 + 1

    # Calculate the total number of decorations in all the boxes
    total_tinsel = tinsel_per_box * total_boxes
    total_tree = tree_per_box * total_boxes
    total_snowglobe = snowglobe_per_box * total_boxes

    # Calculate the total number of decorations
    total_decorations = total_tinsel + total_tree + total_snowglobe

    result = total_decorations
    return result

print(solution())