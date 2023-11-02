def solution():
    # Calculate total gallons of fertilizer needed
    total_acres = 20
    fertilizer_per_acre = 400
    total_fertilizer = total_acres * fertilizer_per_acre

    # Calculate how many days it will take to spread the fertilizer
    acres_per_day = 4
    horses = 80
    fertilizer_per_horse_per_day = 5
    total_fertilizer_per_day = horses * fertilizer_per_horse_per_day
    days_to_spread_fertilizer = total_fertilizer / total_fertilizer_per_day / acres_per_day

    result = days_to_spread_fertilizer
    return result

print(solution())