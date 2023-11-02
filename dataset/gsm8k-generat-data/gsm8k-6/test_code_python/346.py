def solution():
    # Calculate the total area of the four walls
    wall1 = 3 * 2  # area of first wall
    wall2 = 3 * 2  # area of second wall
    wall3 = 5 * 2  # area of third wall
    wall4 = 4 * 2  # area of fourth wall
    total_area = wall1 + wall2 + wall3 + wall4

    # Calculate the number of cans of paint Lucille needs
    cans_of_paint = total_area / 2  # each can of paint covers 2 square meters
    result = cans_of_paint
    return result

print(solution())