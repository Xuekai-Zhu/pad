def solution():
    """Cassy packs 12 jars of jam in 10 boxes while she packs 10 jars of jam in 30 boxes.
    If she has 500 jars of jams, how many jars of jam will she have left when all the boxes are full?"""
    # Define the number of jars per box for each scenario
    jars_per_box_1 = 12/10  # 1.2 jars per box
    jars_per_box_2 = 10/30  # 1/3 jars per box

    # Calculate how many boxes of each type Cassy needs
    num_boxes_1 = 500 / jars_per_box_1
    num_boxes_2 = 500 / jars_per_box_2

    # Round up to the nearest whole number since you can't have a fraction of a box
    num_boxes_1 = math.ceil(num_boxes_1)
    num_boxes_2 = math.ceil(num_boxes_2)

    # Calculate how many jars will be used for each type of box
    num_jars_1 = num_boxes_1 * jars_per_box_1
    num_jars_2 = num_boxes_2 * jars_per_box_2

    # Calculate how many jars will be left over when all boxes are full
    num_jars_left = 500 - num_jars_1 - num_jars_2

    result = num_jars_left
    return result

print(solution())