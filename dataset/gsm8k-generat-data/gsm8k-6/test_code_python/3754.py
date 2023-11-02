def solution():
    # Find the number of teeth of each shark
    hammerhead_teeth = 1/6 * 180
    tiger_teeth = 180
    great_white_teeth = 2 * (hammerhead_teeth + tiger_teeth)

    result = great_white_teeth
    return result

print(solution())