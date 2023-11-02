def solution():
    """Brandon has been fired from half the businesses in town and has quit from a third of them. If there are 72 business in town, how many businesses can he still apply to?"""
    businesses_in_town = 72
    businesses_fired_from = businesses_in_town / 2
    businesses_quit_from = businesses_in_town / 3
    remaining_businesses = businesses_in_town - businesses_fired_from - businesses_quit_from
    result = remaining_businesses
    return result

print(solution())