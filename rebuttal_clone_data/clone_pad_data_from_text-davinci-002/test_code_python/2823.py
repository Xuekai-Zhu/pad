def solution():
     apples_sold = 720
     apples_per_box = 10
     total_boxes = apples_sold / apples_per_box
     boxes_sold_sat = 50
     boxes_sold_sun = 25
     boxes_left = total_boxes - (boxes_sold_sat + boxes_sold_sun)
     result = boxes_left
     return result

print(solution())