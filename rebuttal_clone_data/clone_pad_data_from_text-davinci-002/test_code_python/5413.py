def solution():
     sugar_snap_peas_picked = 56
     minutes_to_pick = 7
     peas_per_minute = sugar_snap_peas_picked / minutes_to_pick
     sugar_snap_peas_to_pick = 72
     minutes_needed = sugar_snap_peas_to_pick / peas_per_minute
     result = minutes_needed
     return result

print(solution())