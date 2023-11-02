def solution():
    """A Printing shop needs to ship 5000 brochures to an advertising company. Each box can only contain one-fifth of the brochures. How many boxes are needed to ship those brochures?"""
    # Define the total number of brochures
    total_brochures = 5000

    # Calculate the number of brochures per box
    brochures_per_box = total_brochures / 5

    # Calculate the number of boxes needed
    boxes_needed = total_brochures // brochures_per_box

    # Round up to the nearest integer (since each box can only contain a whole number of brochures)
    boxes_needed = math.ceil(boxes_needed)

    # Display the result
    result = boxes_needed
    return result

print(solution())