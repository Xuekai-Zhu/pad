def solution():
     price_per_slice = 7
     slices_per_pie = 6
     number_of_pies = 7
     total_slices = number_of_pies * slices_per_pie
     total_revenue = total_slices * price_per_slice
     result = total_revenue
     return result

print(solution())