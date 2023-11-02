def solution():
    # Define the variables
    car_toll = 12.5
    bike_toll = 7
    car_gas = 3.75
    bike_gas = 3.75
    car_distance = 28 # round trip
    bike_distance = 28 # round trip
    car_mpg = 35
    bike_mpg = 35
    car_days = 3
    bike_days = 2

    # Calculate the total cost for the car
    car_total_distance = car_distance * car_days
    car_gas_cost = car_gas * (car_total_distance / car_mpg)
    car_toll_cost = car_toll * car_days
    car_total_cost = car_gas_cost + car_toll_cost

    # Calculate the total cost for the bike
    bike_total_distance = bike_distance * bike_days
    bike_gas_cost = bike_gas * (bike_total_distance / bike_mpg)
    bike_toll_cost = bike_toll * bike_days
    bike_total_cost = bike_gas_cost + bike_toll_cost

    # Calculate the total cost
    total_cost = car_total_cost + bike_total_cost
    result = total_cost
    return result

print(solution())