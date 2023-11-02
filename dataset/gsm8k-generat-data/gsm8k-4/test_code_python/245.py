def solution():
    """There are 12 crates that each contain 150 oranges. There are 16 boxes that each hold 30 nectarines. How many pieces of fruit are in the crates and the boxes in total?"""
    # Define the number of crates and the number of oranges per crate
    num_crates = 12
    oranges_per_crate = 150

    # Define the number of boxes and the number of nectarines per box
    num_boxes = 16
    nectarines_per_box = 30

    # Calculate the total number of oranges and nectarines
    total_oranges = num_crates * oranges_per_crate
    total_nectarines = num_boxes * nectarines_per_box

    # Calculate the total number of pieces of fruit
    total_fruit = total_oranges + total_nectarines

    # return the result
    result = total_fruit
    return result

print(solution())