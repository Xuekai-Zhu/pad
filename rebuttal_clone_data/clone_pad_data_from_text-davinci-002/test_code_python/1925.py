def solution():
     lake_speed = 3
     ocean_speed = 2.5
     race_distance = 3
     lake_race_time = race_distance / lake_speed
     ocean_race_time = race_distance / ocean_speed
     total_race_time = (lake_race_time * 5) + (ocean_race_time * 5)
     result = total_race_time
     return result

print(solution())