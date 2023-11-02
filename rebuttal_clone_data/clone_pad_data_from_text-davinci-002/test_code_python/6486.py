def solution():
     east_miles = 30
     west_miles = 50
     miles_per_gallon = 20
     total_miles = 2 * (east_miles + west_miles)
     gallons_used = total_miles / miles_per_gallon
     result = gallons_used
     return result

print(solution())