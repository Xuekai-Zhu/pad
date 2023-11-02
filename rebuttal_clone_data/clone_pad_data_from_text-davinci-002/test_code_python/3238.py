def solution():
     up_speed = 9
     down_speed = 12
     hill_height = 900
     time_up = hill_height / up_speed
     time_down = hill_height / down_speed
     total_time = time_up + time_down
     result = total_time
     return result

print(solution())