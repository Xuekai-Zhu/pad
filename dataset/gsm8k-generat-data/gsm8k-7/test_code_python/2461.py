def solution():
    initial_value = 20000
    annual_depreciation = 1000
    num_years = 6

    # Calculate the current value of Tim's car
    current_value = initial_value - (annual_depreciation * num_years)
    result = current_value
    return result

print(solution())