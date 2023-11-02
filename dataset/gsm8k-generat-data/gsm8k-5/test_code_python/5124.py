def solution():
    # Total amount of fertilizer produced per day
    total_fertilizer_per_day = 5 * 80  # 5 gallons per day per horse, Janet has 80 horses

    # Total amount of fertilizer needed for all 20 acres
    total_fertilizer_needed = 400 * 20  # 400 gallons per acre, 20 acres in total

    # Total days needed to collect enough fertilizer
    days_to_collect = total_fertilizer_needed / total_fertilizer_per_day

    # Total days needed to spread the fertilizer
    days_to_spread = 20 / 4  # Janet can spread fertilizer over 4 acres per day

    # Total days needed for both collecting and spreading the fertilizer
    total_days = days_to_collect + days_to_spread

    result = total_days
    return result

print(solution())