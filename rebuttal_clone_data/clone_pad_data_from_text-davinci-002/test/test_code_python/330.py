def solution():
     fuel_consumption = 5
     first_trip_distance = 30
     second_trip_distance = 20
     total_distance = first_trip_distance + second_trip_distance
     total_fuel_used = total_distance * fuel_consumption
     result = total_fuel_used
     return result

print(solution())