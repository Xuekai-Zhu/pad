def solution():
    # Calculate the volume of conditioner Sarah uses daily
    conditioner = 1/2  # conditioner is half as much as shampoo
    total_daily_volume = 1 + conditioner  # total volume of shampoo and conditioner used daily
    two_weeks = 14  # number of days in two weeks
    total_volume_used = two_weeks * total_daily_volume  # total volume of shampoo and conditioner used in two weeks
    result = total_volume_used
    return result

print(solution())