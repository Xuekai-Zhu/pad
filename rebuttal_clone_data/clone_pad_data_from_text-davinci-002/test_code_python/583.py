def solution():
     largest_hole_rate = 3
     medium_hole_rate = largest_hole_rate / 2
     smallest_hole_rate = medium_hole_rate / 3
     total_rate = largest_hole_rate + medium_hole_rate + smallest_hole_rate
     time = 2
     total_amount = total_rate * time
     result = total_amount
     return result

print(solution())