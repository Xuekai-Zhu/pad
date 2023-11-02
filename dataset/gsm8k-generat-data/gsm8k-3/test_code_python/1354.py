def solution():
    """Archie needs to lay sod in his backyard that measures 20 yards by 13 yards. He has a shed on it that measures 3 yards by 5 yards. How many square yards of sod will Archie need for his backyard?"""
    # Calculate the total area of the backyard
    backyard_area = 20 * 13

    # Calculate the area of the shed
    shed_area = 3 * 5

    # Calculate the area of the backyard without the shed
    actual_backyard_area = backyard_area - shed_area

    # Calculate the area in square yards
    square_yard_area = actual_backyard_area / 9

    # Display the result
    result = square_yard_area
    return result

print(solution())