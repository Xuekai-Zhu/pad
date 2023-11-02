def solution():
     total_slices = 2 * 12
     eaten_slices = total_slices * 0.25
     remaining_slices = total_slices - eaten_slices
     eaten_slices = remaining_slices * 0.5
     final_slices = remaining_slices - eaten_slices
     result = final_slices
     return result

print(solution())