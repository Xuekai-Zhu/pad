def solution():
     base_points = 10
     kill_bonus = 50
     kill_requirement = 100
     kills = 150
     total_points = base_points * kills
 
     if kills >= kill_requirement:
         total_points = total_points + (total_points * (kill_bonus / 100))
 
     result = total_points
     return result

print(solution())