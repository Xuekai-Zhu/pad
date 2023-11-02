def solution():
    # Define the capacity of the gas tanks
    truck_tank_capacity = 20
    car_tank_capacity = 12

    # Calculate how much gas is already in each tank
    truck_current_gas = truck_tank_capacity / 2
    car_current_gas = car_tank_capacity / 3

    # Calculate how much gas needs to be added to each tank to fill them up completely
    truck_gas_to_add = truck_tank_capacity - truck_current_gas
    car_gas_to_add = car_tank_capacity - car_current_gas

    # Calculate the total gas that needs to be added
    total_gas_to_add = truck_gas_to_add + car_gas_to_add
    result = total_gas_to_add
    return result

print(solution())