def solution():
    
    lake_speed = 3
    ocean_speed = 2.5
    race_distance = 3
    lake_races = 5
    ocean_races = 5
    lake_time = (race_distance / lake_speed) * lake_races
    ocean_time = (race_distance / ocean_speed) * ocean_races
    total_time = lake_time + ocean_time
    result = total_time
    return result

print(solution())