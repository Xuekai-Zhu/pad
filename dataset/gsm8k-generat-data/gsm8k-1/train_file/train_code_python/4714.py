def solution():
    """Mary is paying her monthly garbage bill for a month with exactly four weeks. The garbage company charges Mary $10 per trash bin and $5 per recycling bin every week, and Mary has 2 trash bins and 1 recycling bin. They're giving her an 18% discount on the whole bill before fines for being elderly, but also charging her a $20 fine for putting inappropriate items in a recycling bin. How much is Mary's garbage bill?"""
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