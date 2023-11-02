def solution():
    num_boxes = 2
    pencils_per_box = 14
    pencils_given_away = 6

    # Calculate the total number of pencils Ashton had initially
    total_pencils = num_boxes * pencils_per_box

    # Subtract the number of pencils given away
    pencils_left = total_pencils - pencils_given_away
    result = pencils_left
    return result

print(solution())