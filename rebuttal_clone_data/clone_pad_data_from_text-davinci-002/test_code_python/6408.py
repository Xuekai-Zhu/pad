def solution():
     total_time = 67
     time_building = 3 * time_planning - 5
     time_planning = (total_time + 5) / 3
     result = time_building
     return result

print(solution())