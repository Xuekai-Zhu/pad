def solution():
     wall1_width = 3
     wall1_height = 2
     wall2_width = 5
     wall2_height = 2
     wall3_width = 4
     wall3_height = 2
     wall1_area = wall1_width * wall1_height
     wall2_area = wall2_width * wall2_height
     wall3_area = wall3_width * wall3_height
     total_area = wall1_area + wall2_area + wall3_area
     paint_cans_needed = total_area / 2
     result = paint_cans_needed
     return result

print(solution())