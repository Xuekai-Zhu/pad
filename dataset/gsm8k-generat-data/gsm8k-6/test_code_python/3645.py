def solution():
    # Calculate the total cost of gas for one round trip to work
    gas_cost = 3.75 * (14 / 35)  # gas cost for 14 mile round trip
    # Calculate the total cost of tolls for one week
    car_toll = 12.50 * 3  # Geordie drives his car to work three times a week
    bike_toll = 7 * 2  # Geordie drives his bike to work twice a week
    total_toll_cost = car_toll + bike_toll
    # Calculate the total amount spent driving to work and back in a week
    total_cost = total_toll_cost + (gas_cost * 5)  # Geordie works five days a week
    result = total_cost
    return result

print(solution())