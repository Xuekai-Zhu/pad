def solution():
     bricks_per_course = 10
     courses_per_wall = 6
     walls = 4
     courses_incomplete = 2
     bricks_used = (walls * courses_per_wall * bricks_per_course) - (courses_incomplete * bricks_per_course)
     result = bricks_used
     return result

print(solution())