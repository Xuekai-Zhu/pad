def solution():
     first_place_points = (12 * 2) + (4 * 1)
     second_place_points = (13 * 2) + (1 * 1)
     third_place_points = (8 * 2) + (10 * 1)
     total_points = first_place_points + second_place_points + third_place_points
     average_points = total_points / 3
     result = average_points
     return result

print(solution())