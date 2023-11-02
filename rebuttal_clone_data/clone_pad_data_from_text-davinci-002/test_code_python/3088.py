def solution():
     liters_per_gallon = 8
     miles_per_gallon = 40
     destination_distance = 280
     round_trip_distance = destination_distance * 2
     total_gallons_needed = round_trip_distance / miles_per_gallon
     total_liters_needed = total_gallons_needed * liters_per_gallon
     result = total_liters_needed
     return result

print(solution())