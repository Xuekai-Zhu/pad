def solution():
    """The Jacksonville Walmart normally gets 120 customer complaints per day. That number increases by 1/3rd when they're short-staffed and this increases by another 20% when the self-checkout is broken. If the store was short-staffed and the self-checkout was broken for 3 days, how many complaints does the store get?"""
    normal_complaints_per_day = 120
    short_staffed_increase = normal_complaints_per_day / 3
    broken_self_checkout_increase = short_staffed_increase * 0.2
    total_complaints_per_day = normal_complaints_per_day + short_staffed_increase + broken_self_checkout_increase
    complaints_for_3_days = total_complaints_per_day * 3
    result = complaints_for_3_days
    return result

print(solution())