def solution():
    """Arnold owns three cars. The first car averages 50 miles per gallon of gas. The second car averages 10 miles per gallon of gas. And the third car averages 15 miles per gallon of gas. He splits his 450-mile monthly driving mileage equally amongst his three cars. If gas costs $2 per gallon, how much does he spend on gas each month?"""
    # Define the average miles per gallon for each car
    car_1_mpg = 50
    car_2_mpg = 10
    car_3_mpg = 15

    # Define the monthly driving mileage
    total_mileage = 450

    # Calculate the mileage each car will be driven
    car_mileage = total_mileage / 3

    # Calculate the amount of gas needed for each car
    car_1_gas = car_mileage / car_1_mpg
    car_2_gas = car_mileage / car_2_mpg
    car_3_gas = car_mileage / car_3_mpg

    # Calculate the total amount spent on gas
    total_gas_cost = (car_1_gas + car_2_gas + car_3_gas) * 2

    # Return the result
    result = total_gas_cost
    return result

print(solution())