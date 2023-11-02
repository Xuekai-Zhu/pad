def solution():
     floors = 12
     minutes_per_floor = 2
     meters_per_floor = 800
     seconds_per_meter = 10
     total_seconds = minutes_per_floor * floors * seconds_per_meter * meters_per_floor
     result = total_seconds
     return result

print(solution())