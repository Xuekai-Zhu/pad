def solution():
    
    trash_bins = 2
    recycling_bins = 1
    cost_per_trash_bin_per_week = 10
    cost_per_recycling_bin_per_week = 5
    weeks_in_month = 4
    pre_discount_total = (trash_bins * cost_per_trash_bin_per_week + recycling_bins * cost_per_recycling_bin_per_week) * weeks_in_month
    discount_percent = 18
    discounted_total = pre_discount_total - (pre_discount_total * (discount_percent / 100))
    recycling_fine = 20
    final_total = discounted_total + recycling_fine
    result = final_total
    return result

print(solution())