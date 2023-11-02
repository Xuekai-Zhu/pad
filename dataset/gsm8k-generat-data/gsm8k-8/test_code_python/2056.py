def solution():
    # Calculate the number of wipes used per day
    wipes_per_day = 2 * 1 # 2 walks per day, 1 wipe per walk

    # Calculate the total number of wipes needed for 360 days
    total_wipes_needed = 360 * wipes_per_day

    # Calculate the number of packs needed, rounding up to the nearest whole number
    packs_needed = int(total_wipes_needed / 120) + (total_wipes_needed % 120 > 0)

    result = packs_needed
    return result

print(solution())