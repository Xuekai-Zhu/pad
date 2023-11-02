def solution():
    asparagus_per_day = 0.25
    broccoli_per_day = 0.25
    weeks = 2
    new_asparagus_amount = asparagus_per_day * 2 * 7 * weeks
    new_broccoli_amount = broccoli_per_day * 2 * 7 * weeks
    kale_per_week = 3
    total_vegetables_per_week = new_asparagus_amount + new_broccoli_amount + kale_per_week
    result = total_vegetables_per_week
    return result

print(solution())