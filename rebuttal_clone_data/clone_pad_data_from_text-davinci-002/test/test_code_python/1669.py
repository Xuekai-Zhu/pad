def solution():
     legos_per_side_1 = 7
     legos_per_side_2 = legos_per_side_1 - 1
     legos_per_side_3 = legos_per_side_2 - 1
     total_legos = (legos_per_side_1 * legos_per_side_1) + (legos_per_side_2 * legos_per_side_2) + (legos_per_side_3 * legos_per_side_3)
     result = total_legos
     return result

print(solution())