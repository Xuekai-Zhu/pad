def solution():
    mpg = 25
    daily_mileage = 50
    num_work_days = 5
    tank_size = 10
    gas_price = 2

    # Calculate the weekly gas usage in gallons
    weekly_gas_usage = (daily_mileage * num_work_days) / mpg

    # Calculate how many times Tony needs to fill up his tank each week
    fills_per_week = weekly_gas_usage / tank_size

    # Calculate the weekly cost of gas
    weekly_gas_cost = fills_per_week * tank_size * gas_price

    # Calculate the total cost of gas in 4 weeks
    total_gas_cost = weekly_gas_cost * 4
    result = total_gas_cost
    return result

print(solution())