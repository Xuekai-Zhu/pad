def solution():
    """Hannah's AdBlock blocks all but 20% of ads, and 20% of the ads it doesn't block are actually interesting. What percentage of ads aren't interested and don't get blocked?"""
    # Calculate the percentage of ads that get blocked
    blocked_percentage = 80

    # Calculate the percentage of ads that don't get blocked
    unblocked_percentage = 100 - blocked_percentage

    # Calculate the percentage of unblocked ads that are not interesting
    not_interesting_percentage = unblocked_percentage * 0.8

    # Calculate the percentage of unblocked ads that are interesting
    interesting_percentage = unblocked_percentage * 0.2

    # Calculate the percentage of unblocked ads that aren't interesting and don't get blocked
    not_interesting_and_unblocked_percentage = not_interesting_percentage - (interesting_percentage * 0.2)

    # Display the percentage of unblocked ads that aren't interesting and don't get blocked
    result = not_interesting_and_unblocked_percentage
    return result

print(solution())