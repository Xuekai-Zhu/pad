def solution():
    # Define the number of brochures and the fraction of brochures in one box
    num_brochures = 5000
    fraction_per_box = 1/5

    # Calculate the number of boxes needed to ship all the brochures
    num_boxes = num_brochures / fraction_per_box
    result = num_boxes
    return result

print(solution())