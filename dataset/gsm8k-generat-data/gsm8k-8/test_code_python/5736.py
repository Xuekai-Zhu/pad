def solution():
    # Define the number of pencils per box and the number of boxes
    pencils_per_box = 14
    num_boxes = 2

    # Calculate the total number of pencils
    total_pencils = pencils_per_box * num_boxes

    # Subtract the pencils given away
    remaining_pencils = total_pencils - 6
    result = remaining_pencils
    return result

print(solution())