def solution():
    # Define the known quantities
    ending_boxes = 4
    given_away = (ending_boxes * 2) - 1
    initial_boxes = given_away * 2

    # Subtract the box given to his mother
    initial_boxes -= 1
    result = initial_boxes
    return result

print(solution())