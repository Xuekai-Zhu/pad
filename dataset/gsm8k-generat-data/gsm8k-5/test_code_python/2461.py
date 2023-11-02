def solution():
    car_value = 20000  # Tim bought the car for $20,000
    depreciation_per_year = 1000  # The car goes down in value by $1000 a year
    years_owned = 6  # Tim has owned the car for 6 years

    # Calculate the current value of the car
    current_value = car_value - (depreciation_per_year * years_owned)
    result = current_value
    return result

print(solution())