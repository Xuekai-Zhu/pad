def solution():
    ounces_of_dry_tea_leaves = 28
    ounces_used_daily = 0.20
    ounces_in_a_week = 7
    cups_of_tea_from_one_box = ounces_of_dry_tea_leaves / ounces_used_daily
    weeks_of_tea = cups_of_tea_from_one_box / ounces_in_a_week
    result = weeks_of_tea
    return result

print(solution())