def solution():
    """A courier received 80 packages yesterday and twice as many today. All of these should be delivered tomorrow. How many packages should be delivered tomorrow?"""
    # Define the number of packages received yesterday and today
    packages_yesterday = 80
    packages_today = 2 * packages_yesterday

    # Calculate the total number of packages to be delivered tomorrow
    packages_tomorrow = packages_yesterday + packages_today

    # return the result
    result = packages_tomorrow
    return result

print(solution())