def solution():
     trip_distance = 140
     car_efficiency = 10
     first_part_distance = car_efficiency * 2
     second_part_distance = trip_distance - first_part_distance
     gasoline_used = (first_part_distance / car_efficiency) + (second_part_distance / car_efficiency)
     result = gasoline_used
     return result

print(solution())