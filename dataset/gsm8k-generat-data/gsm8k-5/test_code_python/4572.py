def solution():
    ounces_per_bottle = 16  # Jon drinks a 16-ounce bottle every 4 hours
    awake_hours_per_day = 16  # Jon is awake for 16 hours each day
    bottles_per_day = awake_hours_per_day / 4  # Jon drinks a bottle every 4 hours
    regular_bottles_per_week = bottles_per_day * 7  # Jon drinks this many regular bottles per week
    larger_bottles_per_day = 2  # Jon drinks 2 larger bottles per day
    larger_bottle_size = 1.25 * ounces_per_bottle  # Jon's larger bottles are 25% larger than his regular bottles
    larger_bottles_per_week = larger_bottles_per_day * 7  # Jon drinks this many larger bottles per week

    # Calculate the total fluid Jon drinks per week, assuming he drinks the same amount every day
    total_fluid_per_week = (regular_bottles_per_week * ounces_per_bottle) + (larger_bottles_per_week * larger_bottle_size)
    result = total_fluid_per_week
    return result

print(solution())