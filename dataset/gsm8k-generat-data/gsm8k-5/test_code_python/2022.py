def solution():
    daily_consumption = 500  # Dana normally drinks 500 ml of soda each day
    total_volume = 2000  # Dana buys a 2-liter bottle of soda
    num_days = (total_volume * 1000) / daily_consumption  # Calculate how many days the 2L bottle will last

    result = num_days
    return result

print(solution())