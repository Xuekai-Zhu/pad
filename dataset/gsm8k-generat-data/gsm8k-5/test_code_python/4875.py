def solution():
    water_per_day = 72  # Tony drinks 72 ounces of water per day
    water_bottle_size = 84  # Tony buys an 84-ounce metal water bottle

    # Calculate the number of times Tony will fill his water bottle each day
    fills_per_day = water_per_day / water_bottle_size

    # Multiply the number of fills per day by the number of days in a week
    fills_per_week = fills_per_day * 7
    result = fills_per_week
    return result

print(solution())