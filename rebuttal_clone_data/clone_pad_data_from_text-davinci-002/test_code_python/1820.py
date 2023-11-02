def solution():
     chocolates = 50
     filled_boxes = 3
     chocolates_not_in_boxes = 5
     friend_chocolates = 25
     total_chocolates = chocolates + friend_chocolates
     total_boxes = total_chocolates / chocolates_not_in_boxes
     result = total_boxes - filled_boxes
     return result

print(solution())