def solution():
    """Free Christmas decorations are being given out to families. Each box of decorations contains 4 pieces of tinsel, 1 Christmas tree and 5 snow globes. If 11 families receive a box of decorations and another box is given to the community center, how many decorations have been handed out?"""
    pieces_of_tinsel_per_box = 4
    christmas_trees_per_box = 1
    snow_globes_per_box = 5
    boxes_given_to_families = 11
    boxes_given_to_community_center = 1
    
    total_tinsel = pieces_of_tinsel_per_box * (boxes_given_to_families + boxes_given_to_community_center)
    total_trees = christmas_trees_per_box * (boxes_given_to_families + boxes_given_to_community_center)
    total_snow_globes = snow_globes_per_box * (boxes_given_to_families + boxes_given_to_community_center)
    
    total_decorations = total_tinsel + total_trees + total_snow_globes
    result = total_decorations
    return result

print(solution())