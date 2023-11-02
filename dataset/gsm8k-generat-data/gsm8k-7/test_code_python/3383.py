def solution():
    blocked_ads = 0.8  # AdBlock blocks 80% of ads
    not_blocked_ads = 1 - blocked_ads  # Find the percentage of ads that aren't blocked
    non_interesting_ads = 0.8  # 20% of the ads aren't blocked and aren't interesting
    interesting_ads = 0.2  # 20% of the ads aren't blocked and are interesting

    # Calculate the percentage of ads that aren't interesting and aren't blocked
    non_interesting_unblocked_ads = not_blocked_ads * non_interesting_ads

    # Convert the percentage to a decimal and round to two decimal places
    result = round(non_interesting_unblocked_ads, 2)
    return result

print(solution())