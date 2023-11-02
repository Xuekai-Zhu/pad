def solution():
    
    tiger_shark_teeth = 180
    hammerhead_shark_teeth = tiger_shark_teeth / 6
    great_white_shark_teeth = 2 * (tiger_shark_teeth + hammerhead_shark_teeth)
    result = great_white_shark_teeth
    return result

print(solution())