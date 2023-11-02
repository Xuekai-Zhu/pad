def solution():
    # Calculate how much Thomas saved in the first year
    savings_first_year = 50 * 52  # $50 weekly allowance, 52 weeks in a year

    # Calculate how much Thomas saved in the second year
    savings_second_year = 9 * 30 * 52  # $9 per hour, 30 hours per week, 52 weeks in a year

    # Calculate how much Thomas spent on himself in the second year
    spending_second_year = 35 * 52  # $35 per week, 52 weeks in a year

    # Calculate the total amount of money Thomas saved in 2 years
    total_savings = savings_first_year + savings_second_year - spending_second_year

    # Calculate how much more money Thomas needs to buy the car
    car_price = 15000
    remaining_money = car_price - total_savings
    result = remaining_money
    return result

print(solution())