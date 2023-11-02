def solution():
     car_fuel_cost = 45
     car_fuel_miles = 500
     total_trip_miles = 2000
     total_fuel_cost = car_fuel_cost * (total_trip_miles / car_fuel_miles)
     food_cost = total_fuel_cost * (3/5)
     total_cost = total_fuel_cost + food_cost
     result = total_cost
     return result

print(solution())