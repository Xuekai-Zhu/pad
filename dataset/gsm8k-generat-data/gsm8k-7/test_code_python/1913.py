def solution():
    acres_of_farm = 55
    acres_of_grassland = 30
    plow_rate = 10
    mow_rate = 12

    # Calculate the number of days it will take to plow the farmland
    num_days_to_plow = acres_of_farm / plow_rate

    # Calculate the number of days it will take to mow the grassland
    num_days_to_mow = acres_of_grassland / mow_rate

    # Calculate the total number of days
    total_days = num_days_to_plow + num_days_to_mow

    result = total_days
    return result

print(solution())