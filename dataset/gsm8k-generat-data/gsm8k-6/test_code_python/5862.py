def solution():
    # Calculate the total miles driven by each car
    miles_per_car = 450/3

    # Calculate the total gas used by each car in gallons
    gas_used_car1 = miles_per_car / 50
    gas_used_car2 = miles_per_car / 10
    gas_used_car3 = miles_per_car / 15

    # Calculate the total cost of gas used by all three cars
    total_gas_cost = (gas_used_car1 + gas_used_car2 + gas_used_car3) * 2

    result = total_gas_cost
    return result

print(solution())