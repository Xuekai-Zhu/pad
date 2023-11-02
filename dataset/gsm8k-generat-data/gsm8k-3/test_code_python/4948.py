def solution():
    """Free Christmas decorations are being given out to families. Each box of decorations contains 4 pieces of tinsel, 1 Christmas tree and 5 snow globes. If 11 families receive a box of decorations and another box is given to the community center, how many decorations have been handed out?"""
    # Define the number of decorations in each box
    TINSEL_PER_BOX = 4
    CHRISTMAS_TREE_PER_BOX = 1
    SNOW_GLOBES_PER_BOX = 5

    # Define the number of families receiving decorations
    NUM_FAMILIES = 11

    # Calculate the total number of decorations in all the boxes
    total_tinsel = TINSEL_PER_BOX * (NUM_FAMILIES + 1)  # add 1 box for the community center
    total_christmas_trees = CHRISTMAS_TREE_PER_BOX * (NUM_FAMILIES + 1)
    total_snow_globes = SNOW_GLOBES_PER_BOX * (NUM_FAMILIES + 1)
    total_decorations = total_tinsel + total_christmas_trees + total_snow_globes

    # Display the total number of decorations handed out
    result = total_decorations
    return result

print(solution())