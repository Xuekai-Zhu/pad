def solution():
     smallest_angle = 0
     middle_angle = 3 * smallest_angle
     largest_angle = 5 * smallest_angle
     total_angle = smallest_angle + middle_angle + largest_angle
     given_total_angle = 180
     result = given_total_angle - total_angle
     return result

print(solution())