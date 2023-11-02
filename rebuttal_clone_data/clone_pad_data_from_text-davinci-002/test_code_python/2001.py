def solution():
     first_leg_mph = 60
     first_leg_hours = 2
     second_leg_mph = 50
     second_leg_hours = 3
     miles_per_gallon = 30
     gallons_used = (first_leg_hours * first_leg_mph) / miles_per_gallon + (second_leg_hours * second_leg_mph) / miles_per_gallon
     cost_per_gallon = 2
     total_cost = gallons_used * cost_per_gallon
     result = total_cost
 
     return result

print(solution())