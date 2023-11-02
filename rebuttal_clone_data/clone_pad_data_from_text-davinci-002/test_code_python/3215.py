def solution():
     initial_volume = 500
     hours = 2
     increase_rate = 2/5
     total_increase = initial_volume * (increase_rate * hours)
     final_volume = initial_volume + total_increase
     result = final_volume
     
     return result

print(solution())