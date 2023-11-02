def solution():
    eddie_daily_pies = 3
    sister_daily_pies = 6
    mother_daily_pies = 8
    num_days = 7

    # Calculate the total number of pies that can be baked in one day
    total_daily_pies = eddie_daily_pies + sister_daily_pies + mother_daily_pies

    # Calculate the total number of pies that can be baked in 7 days
    total_pies = total_daily_pies * num_days
    result = total_pies
    return result

print(solution())