def solution():
    quarters_per_day = 1
    days_josiah_saves = 24
    total_josiah_saves = quarters_per_day * days_josiah_saves * 0.25

    cents_per_day_leah = 50
    days_leah_saves = 20
    total_leah_saves = cents_per_day_leah * days_leah_saves * 0.01

    total_megan_saves = total_leah_saves * 2 * 12 * 0.01

    total_savings = total_josiah_saves + total_leah_saves + total_megan_saves
    result = total_savings
    return result

print(solution())