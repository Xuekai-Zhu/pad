def solution():
    initial_fuel = 47  # John's car's tank is initially filled with 47 liters of gasoline
    final_fuel = 14  # After a journey of 275 km, there are 14 liters of gasoline left in the tank
    distance_traveled = 275  # John traveled 275 km

    fuel_consumed = initial_fuel - final_fuel  # Calculate the total fuel consumed during the journey
    fuel_consumption_per_kilometer = fuel_consumed / distance_traveled  # Calculate the fuel consumption per kilometer
    fuel_consumption_per_100km = fuel_consumption_per_kilometer * 100  # Convert the fuel consumption to per 100 km

    result = fuel_consumption_per_100km
    return result

print(solution())