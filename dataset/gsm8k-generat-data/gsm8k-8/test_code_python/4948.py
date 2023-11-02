def solution():
    # Calculate the number of decorations in one box
    tinsel_per_box = 4
    christmas_trees_per_box = 1
    snow_globes_per_box = 5
    decorations_per_box = tinsel_per_box + christmas_trees_per_box + snow_globes_per_box

    # Calculate the total number of decorations in all boxes
    total_decorations = decorations_per_box * 12

    result = total_decorations
    return result

print(solution())