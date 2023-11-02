def solution():
    decorations_per_box = 4 + 1 + 5  # Each box contains 4 pieces of tinsel, 1 Christmas tree and 5 snow globes
    families = 11  # 11 families receive a box of decorations
    community_center = 1  # 1 box is given to the community center

    # Calculate the total number of decorations handed out
    total_decorations = (families + community_center) * decorations_per_box
    result = total_decorations
    return result

print(solution())