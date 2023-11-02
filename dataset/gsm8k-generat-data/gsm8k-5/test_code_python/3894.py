def solution():
    mpg = 25  # Tony's car gets 25 miles to the gallon
    work_distance = 50  # Tony drives 50 miles round trip to work
    work_days = 5  # Tony works 5 days a week
    tank_size = 10  # Tony's tank holds 10 gallons
    gas_price = 2  # Tony pays $2 per gallon of gas

    # Calculate the total distance Tony drives in a week
    weekly_distance = work_distance * work_days

    # Calculate how many gallons of gas Tony uses in a week
    weekly_gas_used = weekly_distance / mpg

    # Calculate how many times Tony needs to fill up his tank in a week
    weekly_fillups = weekly_gas_used / tank_size
    weekly_fillups = math.ceil(weekly_fillups)

    # Calculate Tony's weekly gas cost
    weekly_gas_cost = weekly_fillups * tank_size * gas_price

    # Calculate Tony's total gas cost for 4 weeks
    total_gas_cost = weekly_gas_cost * 4
    result = total_gas_cost
    return result

print(solution())