def solution():
    """Arnold owns three cars. The first car averages 50 miles per gallon of gas. The second car averages 10 miles per gallon of gas. And the third car averages 15 miles per gallon of gas. He splits his 450-mile monthly driving mileage equally amongst his three cars.  If gas costs $2 per gallon, how much does he spend on gas each month?"""
    # Define the average miles per gallon for each car
    CAR1_MPG = 50
    CAR2_MPG = 10
    CAR3_MPG = 15

    # Define the total monthly driving mileage
    TOTAL_MILEAGE = 450

    # Calculate the mileage each car will drive
    car_mileage = TOTAL_MILEAGE / 3

    # Calculate the total gallons of gas used by each car
    car1_gas = car_mileage / CAR1_MPG
    car2_gas = car_mileage / CAR2_MPG
    car3_gas = car_mileage / CAR3_MPG

    # Calculate the total cost of gas used by all three cars
    total_gas_cost = (car1_gas + car2_gas + car3_gas) * 2

    # Display the total cost of gas
    result = total_gas_cost
    return result

print(solution())