def solution():
    time_1 = 21 # hours
    fuel_1 = 7 # liters

    time_2 = 90 # hours

    # Calculate the fuel consumption rate (liters per hour)
    fuel_rate = fuel_1 / time_1

    # Calculate the fuel consumption over 90 hours
    fuel_2 = fuel_rate * time_2
    result = fuel_2
    return result

print(solution())