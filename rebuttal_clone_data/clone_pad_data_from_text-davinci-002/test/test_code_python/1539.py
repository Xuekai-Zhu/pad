def solution():
     total_laps = 98
     laps_swam_on_saturday = 27
     laps_swam_on_sunday = 15
     laps_swam_total = laps_swam_on_saturday + laps_swam_on_sunday
     laps_remaining = total_laps - laps_swam_total
     result = laps_remaining
     return result

print(solution())