def solution():
    """James has a room that is 13 feet by 18 feet. He increases each dimension by 2 feet. He then builds 3 more rooms of equal size and 1 room of twice that size. How much area does he have?"""
    # Define the dimensions of the original room
    original_width = 13
    original_length = 18

    # Calculate the dimensions of the enlarged room
    enlarged_width = original_width + 2
    enlarged_length = original_length + 2

    # Calculate the area of the enlarged room
    enlarged_area = enlarged_width * enlarged_length

    # Calculate the area of the original room
    original_area = original_width * original_length

    # Calculate the area of the 3 new rooms
    new_area = 3 * enlarged_area

    # Calculate the area of the larger new room
    larger_new_area = 2 * enlarged_area

    # Calculate the total area
    total_area = original_area + new_area + larger_new_area

    result = total_area
    return result

print(solution())