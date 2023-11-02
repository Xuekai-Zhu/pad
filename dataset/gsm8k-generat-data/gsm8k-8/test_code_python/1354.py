def solution():
    # Calculate the total area of the backyard
    backyard_area = 20 * 13

    # Calculate the area of the shed
    shed_area = 3 * 5

    # Subtract the area of the shed from the total area of the backyard
    sod_area = backyard_area - shed_area
    result = sod_area
    return result

print(solution())