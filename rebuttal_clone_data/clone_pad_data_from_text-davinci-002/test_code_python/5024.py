def solution():
     initial_hours = 8
     hours_increased = initial_hours * (75 / 100)
     total_hours = initial_hours + hours_increased
     initial_speed = 8
     speed_increased = 4
     total_speed = initial_speed + speed_increased
     total_distance = total_hours * total_speed
     result = total_distance
     return result

print(solution())