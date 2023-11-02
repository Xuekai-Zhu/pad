def solution():
    initial_height = 48
    target_height = 54
    height_increase_monthly = initial_height * (1/3)
    height_increase_hourly = initial_height * (1/12)
    hours_neede_monthly = height_increase_monthly / height_increase_hourly
    result = hours_neede_monthly
    
    return result

print(solution())