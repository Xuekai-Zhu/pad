def solution():
     
     families = 3
     people_per_family = 4
     days_of_use = 7
     towels_used = families * people_per_family * days_of_use
     towels_per_load = 14
     loads_of_laundry = towels_used / towels_per_load
     result = loads_of_laundry
     return result

print(solution())