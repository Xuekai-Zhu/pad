def solution():
    """For a project, a builder purchased 7 boxes of bolts with each box containing 11 bolts. He purchased 3 boxes of nuts with each box containing 15 nuts. He ended up finishing the project 6 days early and with 3 bolts and 6 nuts left over. How many bolts and nuts did he use for the project?"""
    # Define the number of bolts and nuts per box
    bolts_per_box = 11
    nuts_per_box = 15

    # Define the number of boxes purchased
    bolts_boxes = 7
    nuts_boxes = 3

    # Calculate the total number of bolts and nuts purchased
    total_bolts = bolts_per_box * bolts_boxes
    total_nuts = nuts_per_box * nuts_boxes

    # Calculate the total number of bolts and nuts used in the project
    bolts_used = total_bolts - 3
    nuts_used = total_nuts - 6

    # Return the result
    result = (bolts_used, nuts_used)
    return result

print(solution())