def solution():
    # Calculate the total fluid Jon drinks in a day
    small_bottle = 16  # ounces in a small bottle
    large_bottle = 1.25 * small_bottle  # ounces in a large bottle
    small_bottles_per_day = 4  # small bottles Jon drinks every day
    large_bottles_per_day = 2  # large bottles Jon drinks every day
    fluid_per_day = small_bottle * small_bottles_per_day + large_bottle * large_bottles_per_day

    # Calculate the total fluid Jon drinks in a week
    fluid_per_week = fluid_per_day * 7
    result = fluid_per_week
    return result

print(solution())