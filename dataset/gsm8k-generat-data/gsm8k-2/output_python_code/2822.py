def solution():
    """Merry had 50 boxes of apples on Saturday and 25 boxes on Sunday. There were 10 apples in each box. If she sold a total of 720 apples on Saturday and Sunday, how many boxes of apples are left?"""
    saturday_boxes = 50
    sunday_boxes = 25
    apples_per_box = 10
    total_sold_apples = 720
    saturday_apples = saturday_boxes * apples_per_box
    sunday_apples = total_sold_apples - saturday_apples
    remaining_boxes = (saturday_boxes + sunday_boxes) - (sunday_apples // apples_per_box)
    result = remaining_boxes
    return result

print(solution())