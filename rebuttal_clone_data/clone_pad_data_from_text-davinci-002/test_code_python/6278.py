def solution():
     apple_pie_slices = 8
     peach_pie_slices = 6
     apple_pie_customers = 56
     peach_pie_customers = 48
     total_pie_customers = apple_pie_customers + peach_pie_customers
     total_pie_slices = apple_pie_slices + peach_pie_slices
     total_pies_sold = total_pie_customers / total_pie_slices
     
     result = total_pies_sold
     return result

print(solution())