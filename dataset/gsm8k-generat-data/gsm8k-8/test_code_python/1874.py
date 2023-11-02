def solution():
    # Define the number of boxes received and given away
    total_boxes = 45
    given_boxes = 12 + 9 + 7

    # Calculate the number of boxes left for Sonny
    remaining_boxes = total_boxes - given_boxes
    result = remaining_boxes
    return result

print(solution())