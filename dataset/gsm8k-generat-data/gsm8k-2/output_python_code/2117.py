def solution():
    """Brandon has been fired from half the businesses in town and has quit from a third of them. If there are 72 business in town, how many businesses can he still apply to?"""
    total_businesses = 72
    fired_businesses = total_businesses / 2
    quit_businesses = total_businesses / 3
    remaining_businesses = total_businesses - fired_businesses - quit_businesses
    result = remaining_businesses
    return result

print(solution())