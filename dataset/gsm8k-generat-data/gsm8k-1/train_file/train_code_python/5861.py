def solution():
    """Arnold owns three cars. The first car averages 50 miles per gallon of gas. The second car averages 10 miles per gallon of gas. And the third car averages 15 miles per gallon of gas. He splits his 450-mile monthly driving mileage equally amongst his three cars. If gas costs $2 per gallon, how much does he spend on gas each month?"""
    first_car_mpg = 50
    second_car_mpg = 10
    third_car_mpg = 15
    total_monthly_mileage = 450
    percentage_of_mileage_per_car = 1/3
    first_car_gas_used = (percentage_of_mileage_per_car * total_monthly_mileage) / first_car_mpg
    second_car_gas_used = (percentage_of_mileage_per_car * total_monthly_mileage) / second_car_mpg
    third_car_gas_used = (percentage_of_mileage_per_car * total_monthly_mileage) / third_car_mpg
    total_gas_used = first_car_gas_used + second_car_gas_used + third_car_gas_used
    gas_cost_per_gallon = 2
    total_gas_cost = total_gas_used * gas_cost_per_gallon
    result = total_gas_cost
    return result

print(solution())