def solution():
    soda_per_day = 5  # 12-oz cans of soda per day
    water_per_day = 64  # ounces of water per day

    ounces_per_can = 12  # ounces per can of soda
    num_days = 7  # number of days in a week

    # Calculate the total ounces of fluid per day
    total_fluid_per_day = (soda_per_day * ounces_per_can) + water_per_day

    # Calculate the total ounces of fluid per week
    total_fluid_per_week = total_fluid_per_day * num_days
    result = total_fluid_per_week
    return result

print(solution())