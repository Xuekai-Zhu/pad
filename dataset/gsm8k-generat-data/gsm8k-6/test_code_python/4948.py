def solution():
    decorations_per_box = 4 + 1 + 5  # total number of decorations in one box
    total_families = 11 + 1  # 11 families receive a box and another box is given to the community center
    total_decorations = decorations_per_box * total_families  # total number of decorations handed out
    result = total_decorations
    return result

print(solution())