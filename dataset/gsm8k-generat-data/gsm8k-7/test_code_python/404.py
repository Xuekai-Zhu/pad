def solution():
    bales_per_acre = 560 / 5  # bales per acre
    new_acres = 7
    total_acres = 5 + new_acres
    total_bales = total_acres * bales_per_acre

    num_horses = 9
    bales_per_day = 3
    days_in_month = 31
    starting_month = 9
    ending_month = 12

    total_days = (ending_month - starting_month + 1) * days_in_month
    total_hay_consumed = num_horses * bales_per_day * total_days

    hay_left = total_bales - total_hay_consumed
    result = hay_left
    return result

print(solution())