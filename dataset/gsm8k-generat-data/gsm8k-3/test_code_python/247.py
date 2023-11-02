def solution():
    """There are 12 crates that each contain 150 oranges. There are 16 boxes that each hold 30 nectarines. How many pieces of fruit are in the crates and the boxes in total?"""
    # Define the number of crates and oranges per crate
    num_crates_oranges = 12 * 150

    # Define the number of boxes and nectarines per box
    num_boxes_nectarines = 16 * 30

    # Calculate the total number of pieces of fruit
    total_fruit = num_crates_oranges + num_boxes_nectarines

    # Display the total number of pieces of fruit
    result = total_fruit
    return result

print(solution())