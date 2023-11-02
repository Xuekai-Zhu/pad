def solution():
    wipes_per_day = 2  # Randy uses 2 baby wipes per day
    days_per_year = 360  # Randy wants to have enough wipes for 360 days
    wipes_per_pack = 120  # There are 120 wipes per pack

    # Calculate the total number of wipes Randy needs for 1 year
    total_wipes_per_year = wipes_per_day * days_per_year

    # Calculate the total number of packs Randy needs for 1 year
    packs_per_year = total_wipes_per_year / wipes_per_pack

    result = packs_per_year
    return result

print(solution())