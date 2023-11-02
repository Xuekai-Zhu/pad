def solution():
    """Marie, the confectioner, makes 12 chocolate eggs, each weighing 10 ounces. She then packs an equal number of the eggs in 4 different gift boxes. Unfortunately, she leaves one of the boxes by the kitchen window and the afternoon sun melts everything. She tosses that box out. What is the total weight, in ounces, of the remaining chocolate eggs?"""
    # Define the weight of a single egg
    egg_weight = 10

    # Define the number of gift boxes
    num_boxes = 4

    # Calculate the total weight of all the eggs
    total_weight = egg_weight * 12

    # Calculate the weight of a single gift box
    box_weight = total_weight / num_boxes

    # Subtract the weight of the melted box of eggs
    remaining_weight = total_weight - box_weight

    # Return the result
    result = remaining_weight
    return result

print(solution())