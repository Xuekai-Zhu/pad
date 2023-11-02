def solution():
     rainfall_monday = (2 * rainfall_sunday) + 3
     rainfall_tuesday = (2 * rainfall_monday) - 3
     rainfall_sunday = 4
     total_rainfall = rainfall_monday + rainfall_tuesday + rainfall_sunday
     result = total_rainfall
     return result

print(solution())