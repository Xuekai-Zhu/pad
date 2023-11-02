def solution():
     long_sleeved_jersey_cost = 15
     striped_jersey_cost = 10
     total_cost = 80
     total_long_sleeved_jerseys = 4
     total_jerseys = total_cost // (striped_jersey_cost + long_sleeved_jersey_cost)
     striped_jerseys = total_jerseys - total_long_sleeved_jerseys
     result = striped_jerseys
     return result

print(solution())