def solution():
    boxes_given = 12 # 11 families plus 1 community center
    decorations_per_box = 4 + 1 + 5 # 4 tinsel, 1 Christmas tree, 5 snow globes
    total_decorations_given = boxes_given * decorations_per_box
    result = total_decorations_given
    return result

print(solution())