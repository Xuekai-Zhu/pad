def solution():
    gallons_per_day = 5
    acres_per_day = 4
    gallons_per_acre = 400
    total_fertilizer = 80 * gallons_per_day
    total_acres = 20
    acres_left = total_acres
    days_needed = 0
    while acres_left > 0:
        acres_fertilized = min(acres_per_day, acres_left)
        gallons_used = acres_fertilized * gallons_per_acre
        total_fertilizer -= gallons_used
        acres_left -= acres_fertilized
        days_needed += 1
    return days_needed

print(solution())