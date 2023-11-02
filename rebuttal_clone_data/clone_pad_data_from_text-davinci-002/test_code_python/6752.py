def solution():
     apples_per_pie = 4
     apples_used = apples_per_pie * 4
     pie_slices = 6
     apples_per_slice = apples_used / pie_slices
     result = apples_per_slice
     return result

print(solution())