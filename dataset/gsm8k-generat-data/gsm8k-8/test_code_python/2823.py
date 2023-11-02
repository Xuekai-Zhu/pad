def solution():
    # Calculate the total number of apples Merry had
    total_apples = 50 * 10 + 25 * 10

    # Calculate the number of apples sold on Saturday and Sunday
    sold_apples = 720

    # Calculate the number of apples left
    left_apples = total_apples - sold_apples

    # Calculate the number of boxes left
    boxes_left = left_apples // 10

    result = boxes_left
    return result

print(solution())