def solution():
     sum_of_angles = 250
     right_angle = 60
     left_angle = right_angle * 2
     top_angle = sum_of_angles - right_angle - left_angle
     result = top_angle
     return result

print(solution())