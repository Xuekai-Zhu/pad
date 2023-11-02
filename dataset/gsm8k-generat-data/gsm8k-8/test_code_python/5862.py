def solution():
    # Calculate the total miles each car will drive in a month
    miles_per_car = 450 / 3

    # Calculate the total gallons of gas each car will use in a month
    car1_gallons = miles_per_car / 50
    car2_gallons = miles_per_car / 10
    car3_gallons = miles_per_car / 15

    # Calculate the total cost of gas for each car
    car1_cost = car1_gallons * 2
    car2_cost = car2_gallons * 2
    car3_cost = car3_gallons * 2

    # Calculate the total cost of gas for all three cars
    total_gas_cost = car1_cost + car2_cost + car3_cost
    result = total_gas_cost
    return result

print(solution())