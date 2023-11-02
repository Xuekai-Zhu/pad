def solution():
    """Arnold owns three cars. The first car averages 50 miles per gallon of gas. The second car averages 10 miles per gallon of gas. And the third car averages 15 miles per gallon of gas. He splits his 450-mile monthly driving mileage equally amongst his three cars. If gas costs $2 per gallon, how much does he spend on gas each month?"""
    miles_per_month = 450
    car1_mpg = 50
    car2_mpg = 10
    car3_mpg = 15
    total_gallons_used = (miles_per_month / 3) / car1_mpg + (miles_per_month / 3) / car2_mpg + (miles_per_month / 3) / car3_mpg
    gas_price = 2
    total_gas_cost = total_gallons_used * gas_price
    result = total_gas_cost
    return result

print(solution())