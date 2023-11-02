def solution():
    num_brochures = 5000
    brochures_per_box = num_brochures / 5

    # Round up to the nearest whole number of boxes needed
    num_boxes = math.ceil(num_brochures / brochures_per_box)

    result = num_boxes
    return result

print(solution())