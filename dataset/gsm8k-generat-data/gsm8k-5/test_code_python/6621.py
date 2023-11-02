def solution():
    base_complaints = 120  # The Walmart normally gets 120 complaints per day
    shortstaffed_complaints = base_complaints * (1 + (1/3))  # Complaints increase by 1/3 when short-staffed
    broken_checkout_complaints = shortstaffed_complaints * 1.2  # Complaints increase by 20% when the self-checkout is broken

    # Calculate the total number of complaints during the 3 days
    total_complaints = broken_checkout_complaints * 3

    result = total_complaints
    return result

print(solution())