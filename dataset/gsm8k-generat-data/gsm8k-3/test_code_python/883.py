def solution():
    """For a project, a builder purchased 7 boxes of bolts with each box containing 11 bolts.  He purchased 3 boxes of nuts with each box containing 15 nuts. He ended up finishing the project 6 days early and with 3 bolts and 6 nuts left over. How many bolts and nuts did he use for the project?"""
    # Define the number of bolts and nuts in each box
    BOLTS_PER_BOX = 11
    NUTS_PER_BOX = 15

    # Define the number of boxes of bolts and nuts purchased
    bolt_boxes = 7
    nut_boxes = 3

    # Calculate the total number of bolts and nuts purchased
    total_bolts = bolt_boxes * BOLTS_PER_BOX
    total_nuts = nut_boxes * NUTS_PER_BOX

    # Calculate the number of bolts and nuts used for the project
    bolts_used = total_bolts - 3
    nuts_used = total_nuts - 6

    # Display the number of bolts and nuts used for the project
    result = (bolts_used, nuts_used)
    return result

print(solution())