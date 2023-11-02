def solution():
    boxes_saturday = 50
    boxes_sunday = 25
    apples_per_box = 10
    total_apples_sold = 720

    # Calculate the total number of apples Merry had
    total_apples = (boxes_saturday + boxes_sunday) * apples_per_box

    # Calculate the number of apples left
    apples_left = total_apples - total_apples_sold

    # Calculate the number of boxes left
    boxes_left = apples_left // apples_per_box
    result = boxes_left
    return result

print(solution())