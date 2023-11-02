def solution():
    """A Printing shop needs to ship 5000 brochures to an advertising company. Each box can only contain one-fifth of the brochures. How many boxes are needed to ship those brochures?"""
    # Define the number of brochures to be shipped and the fraction of brochures per box
    brochures = 5000
    fraction_per_box = 1/5

    # Calculate the total number of boxes needed
    total_boxes = brochures / fraction_per_box

    # Display the total number of boxes needed
    result = total_boxes
    return result

print(solution())