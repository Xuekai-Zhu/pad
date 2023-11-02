def solution():
    """Merry had 50 boxes of apples on Saturday and 25 boxes on Sunday. There were 10 apples in each box. If she sold a total of 720 apples on Saturday and Sunday, how many boxes of apples are left?"""
    # Define the number of boxes of apples on Saturday and Sunday
    saturday_boxes = 50
    sunday_boxes = 25

    # Calculate the total number of apples on Saturday and Sunday
    total_apples = saturday_boxes * 10 + sunday_boxes * 10

    # Calculate the number of apples sold on Saturday and Sunday
    sold_apples = 720

    # Calculate the number of apples left
    apples_left = total_apples - sold_apples

    # Calculate the number of boxes of apples left
    boxes_left = apples_left // 10

    # return the result
    result = boxes_left
    return result

print(solution())