def solution():
    num_boxes = 2
    pencils_per_box = 12
    lauren_pencils = 6
    matt_pencils = lauren_pencils + 3

    # Calculate the total number of pencils that Steve gave away
    total_given = lauren_pencils + matt_pencils

    # Calculate the total number of pencils that Steve has left
    total_left = (num_boxes * pencils_per_box) - total_given
    result = total_left
    return result

print(solution())