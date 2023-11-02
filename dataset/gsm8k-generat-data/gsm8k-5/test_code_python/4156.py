def solution():
    # Calculate the amount of gas needed to fill the truck's tank
    truck_half_full = 20 / 2
    truck_fill = 20 - truck_half_full

    # Calculate the amount of gas needed to fill the car's tank
    car_one_third_full = 12 / 3
    car_fill = 12 - car_one_third_full

    # Calculate the total amount of gas needed to fill both tanks
    total_gas = truck_fill + car_fill
    result = total_gas
    return result

print(solution())