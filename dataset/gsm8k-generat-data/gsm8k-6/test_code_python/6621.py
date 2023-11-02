def solution():
    daily_complaints = 120  # the normal number of customer complaints per day
    short_staffed_complaints = daily_complaints + (1/3)*daily_complaints  # complaints increase by 1/3 when short-staffed
    broken_checkout_complaints = short_staffed_complaints + (20/100)*short_staffed_complaints  # complaints increase by 20% when self-checkout is broken
    total_complaints = broken_checkout_complaints * 3  # total complaints for 3 days when short-staffed and self-checkout is broken
    result = total_complaints
    return result

print(solution())