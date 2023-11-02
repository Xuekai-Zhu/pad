def solution():
    """Merry had 50 boxes of apples on Saturday and 25 boxes on Sunday. There were 10 apples in each box. If she sold a total of 720 apples on Saturday and Sunday, how many boxes of apples are left?"""
    # Calculate the total number of apples Merry had
    total_apples = 50 * 10 + 25 * 10

    # Calculate the number of apples sold
    sold_apples = 720

    # Calculate the number of apples left
    apples_left = total_apples - sold_apples

    # Calculate the number of boxes of apples left
    boxes_left = apples_left // 10

    # Display the number of boxes of apples left
    result = boxes_left
    return result

print(solution())