def solution():
    """The Jacksonville Walmart normally gets 120 customer complaints per day. That number increases by 1/3rd when they're short-staffed and this increases by another 20% when the self-checkout is broken. If the store was short-staffed and the self-checkout was broken for 3 days, how many complaints does the store get?"""
    # Define the initial number of complaints
    initial_complaints = 120

    # Calculate the number of complaints when short-staffed
    shortstaffed_complaints = initial_complaints + (1/3) * initial_complaints

    # Calculate the number of complaints when the self-checkout is broken
    broken_complaints = shortstaffed_complaints + 0.2 * shortstaffed_complaints

    # Calculate the total number of complaints over 3 days
    total_complaints = 3 * broken_complaints

    # return the result
    result = total_complaints
    return result

print(solution())