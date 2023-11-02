def solution():
     marathon_distance = 20
     current_distance = 2
     weekly_distance = 2/3
     weeks_needed = (marathon_distance - current_distance) / weekly_distance
     result = weeks_needed
     return result

print(solution())