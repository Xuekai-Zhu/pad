def solution():
    """A courier received 80 packages yesterday and twice as many today. All of these should be delivered tomorrow. How many packages should be delivered tomorrow?"""
    packages_yesterday = 80
    packages_today = packages_yesterday * 2
    packages_tomorrow = packages_yesterday + packages_today
    result = packages_tomorrow
    return result

print(solution())