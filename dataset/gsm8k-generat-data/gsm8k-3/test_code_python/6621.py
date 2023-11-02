def solution():
    """The Jacksonville Walmart normally gets 120 customer complaints per day. That number increases by 1/3rd when they're short-staffed and this increases by another 20% when the self-checkout is broken. If the store was short-staffed and the self-checkout was broken for 3 days, how many complaints does the store get?"""
    # Define the normal number of customer complaints per day
    NORMAL_COMPLAINTS = 120

    # Calculate the total number of complaints over 3 days
    short_staffed_complaints = NORMAL_COMPLAINTS * (1 + 1/3)
    broken_checkout_complaints = short_staffed_complaints * 1.2
    total_complaints = broken_checkout_complaints * 3

    # Display the total number of complaints
    result = total_complaints
    return result

print(solution())