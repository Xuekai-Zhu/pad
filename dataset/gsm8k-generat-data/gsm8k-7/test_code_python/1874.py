def solution():
    received_boxes = 45
    brother_boxes = 12
    sister_boxes = 9
    cousin_boxes = 7

    # Calculate the total number of boxes given away
    total_given_away = brother_boxes + sister_boxes + cousin_boxes

    # Calculate the total number of boxes left for Sonny
    total_left = received_boxes - total_given_away

    result = total_left
    return result

print(solution())