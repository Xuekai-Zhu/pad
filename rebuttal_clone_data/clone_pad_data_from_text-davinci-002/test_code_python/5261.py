def solution():
    total_gallons = 1000
    gallons_per_day = total_gallons / 31
    gallons_per_shower = 20
    gallons_per_cubic_foot = 1
    cubic_feet_per_pool = 10 * 10 * 6
    gallons_per_pool = cubic_feet_per_pool * gallons_per_cubic_foot
    showers_per_pool = gallons_per_pool / gallons_per_shower
    showers_per_day = showers_per_pool / days_in_july
    result = showers_per_day
    return result

print(solution())