def solution():
    brochures = 5000  # Total number of brochures to be shipped
    box_capacity = 1/5  # Each box can hold one-fifth of the brochures

    # Calculate the number of boxes needed to ship all the brochures
    boxes_needed = brochures / box_capacity
    result = boxes_needed
    return result

print(solution())