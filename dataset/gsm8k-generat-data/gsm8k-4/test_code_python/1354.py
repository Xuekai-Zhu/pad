def solution():
    """Archie needs to lay sod in his backyard that measures 20 yards by 13 yards. He has a shed on it that measures 3 yards by 5 yards. How many square yards of sod will Archie need for his backyard?"""
    # Define the dimensions of the backyard and the shed
    backyard_width = 20
    backyard_length = 13
    shed_width = 3
    shed_length = 5

    # Calculate the area of the backyard and the shed
    backyard_area = backyard_width * backyard_length
    shed_area = shed_width * shed_length

    # Subtract the area of the shed from the area of the backyard
    sod_area = backyard_area - shed_area

    # Return the result in square yards
    result = sod_area / 1
    return result

print(solution())