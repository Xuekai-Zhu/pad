def solution():
    # Calculate how many gallons Tony uses in one day
    daily_miles = 50
    miles_per_gallon = 25
    daily_gallons = daily_miles / miles_per_gallon

    # Calculate how many days Tony's tank will last
    tank_capacity = 10
    days_per_tank = tank_capacity / daily_gallons

    # Calculate how many fills Tony needs in 4 weeks
    weeks = 4
    fills_needed = weeks * 5 / days_per_tank

    # Calculate how much Tony will spend on gas
    gas_price = 2
    total_spent = fills_needed * tank_capacity * gas_price
    result = total_spent
    return result

print(solution())