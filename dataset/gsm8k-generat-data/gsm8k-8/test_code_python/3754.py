def solution():
    # Define the number of teeth for each shark
    tiger_teeth = 180
    hammerhead_teeth = tiger_teeth / 6
    great_white_teeth = 2 * (tiger_teeth + hammerhead_teeth)

    result = great_white_teeth
    return result

print(solution())