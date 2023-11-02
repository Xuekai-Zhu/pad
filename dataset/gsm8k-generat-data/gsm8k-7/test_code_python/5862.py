def solution():
    car1_mpg = 50
    car2_mpg = 10
    car3_mpg = 15

    total_monthly_mileage = 450
    mileage_per_car = total_monthly_mileage / 3

    # Calculate the total amount of gas needed for each car
    car1_gas = mileage_per_car / car1_mpg
    car2_gas = mileage_per_car / car2_mpg
    car3_gas = mileage_per_car / car3_mpg

    # Calculate the total cost of gas for all cars
    total_gas_cost = (car1_gas + car2_gas + car3_gas) * 2
    result = total_gas_cost
    return result

print(solution())