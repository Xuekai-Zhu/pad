def solution():
    # Calculate the area of the backyard
    backyard_area = 20 * 13

    # Calculate the area of the shed
    shed_area = 3 * 5

    # Calculate the area that needs to be covered with sod
    sod_area = backyard_area - shed_area

    result = sod_area
    return result

print(solution())