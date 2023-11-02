def solution():
     points_max = 5
     points_dulce = 3
     points_val = 2 * (points_max + points_dulce)
     total_points = points_max + points_dulce + points_val
     points_opponents = 40
     points_behind = points_opponents - total_points
     result = points_behind
     return result

print(solution())