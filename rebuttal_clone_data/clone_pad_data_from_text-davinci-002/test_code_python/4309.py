def solution():
     length = 2000
     width = 20
     area = length * width
     truckload_coverage = 800
     number_of_trucks = area / truckload_coverage
     cost_per_truck = 75
     total_cost = number_of_trucks * cost_per_truck
     sales_tax = total_cost * 0.2
     final_cost = total_cost + sales_tax
     result = final_cost
     return result

print(solution())