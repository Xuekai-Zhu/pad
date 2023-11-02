def solution():
    ads_blocked = 0.8  # Hannah's AdBlock blocks 80% of ads
    not_interesting_given_not_blocked = 0.8  # 80% of ads that AdBlock doesn't block aren't interesting
    not_interesting_given_blocked = 0.2 * 0.2  # 20% of ads that AdBlock doesn't block are interesting, so 80% must not be interesting

    # Calculate the percentage of ads that aren't interesting and don't get blocked
    not_interesting_and_not_blocked = (1 - ads_blocked) * not_interesting_given_not_blocked
    result = not_interesting_and_not_blocked * 100
    return result

print(solution())