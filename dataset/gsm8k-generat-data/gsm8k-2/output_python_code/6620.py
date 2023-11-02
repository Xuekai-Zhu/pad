def solution():
    """The Jacksonville Walmart normally gets 120 customer complaints per day. That number increases by 1/3rd when they're short-staffed and this increases by another 20% when the self-checkout is broken. If the store was short-staffed and the self-checkout was broken for 3 days, how many complaints does the store get?"""
    normal_complaints = 120
    short_staffed_increase = normal_complaints * (1/3)
    broken_self_checkout_increase = (normal_complaints + short_staffed_increase) * 0.2
    total_complaints = normal_complaints + short_staffed_increase + broken_self_checkout_increase
    total_complaints *= 3  # multiply by 3 days
    result = total_complaints
    return result

print(solution())