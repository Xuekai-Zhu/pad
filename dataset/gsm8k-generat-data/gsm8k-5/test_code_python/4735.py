def solution():
    cans_per_day = 5  # Tom drinks 5 cans of soda per day
    can_size = 12  # Each can is 12 ounces
    water_per_day = 64  # Tom drinks 64 ounces of water per day
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total fluid Tom drinks from soda
    soda_fluid = cans_per_day * can_size * days_per_week

    # Calculate the total fluid Tom drinks from water
    water_fluid = water_per_day * days_per_week

    # Calculate the total fluid Tom drinks in a week
    total_fluid = soda_fluid + water_fluid
    result = total_fluid
    return result

print(solution())