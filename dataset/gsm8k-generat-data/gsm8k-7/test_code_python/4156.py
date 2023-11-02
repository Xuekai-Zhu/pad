def solution():
    truck_tank = 20
    car_tank = 12
    truck_half_full = truck_tank / 2
    car_one_third_full = car_tank / 3

    # Calculate how much gas is needed to fill up the truck
    truck_gas_needed = truck_tank - truck_half_full

    # Calculate how much gas is needed to fill up the car
    car_gas_needed = car_tank - car_one_third_full

    # Calculate the total gas needed to fill up both vehicles
    total_gas_needed = truck_gas_needed + car_gas_needed
    result = total_gas_needed
    return result

print(solution())