def solution():
    regular_bottle_size = 16  # ounces
    extra_bottle_size = regular_bottle_size * 1.25  # 25% larger
    awake_hours_per_day = 16
    regular_bottles_per_day = awake_hours_per_day / 4

    # Calculate the number of extra bottles per day
    extra_bottles_per_day = 2

    # Calculate the total fluid Jon drinks each day
    total_fluid_per_day = regular_bottles_per_day * regular_bottle_size + extra_bottles_per_day * extra_bottle_size

    # Calculate the total fluid Jon drinks in a week
    total_fluid_per_week = total_fluid_per_day * 7
    result = total_fluid_per_week
    return result

print(solution())