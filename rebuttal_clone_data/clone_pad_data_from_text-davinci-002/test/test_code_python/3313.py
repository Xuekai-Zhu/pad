def solution():
     box_1_capacity = 80
     box_2_capacity = 50
     box_1_filled = box_1_capacity * 3/4
     box_2_filled = box_2_capacity * 3/5
     total_oranges = box_1_filled + box_2_filled
     result = total_oranges
     return result

print(solution())