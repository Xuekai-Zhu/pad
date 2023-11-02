def solution():
    """A courier received 80 packages yesterday and twice as many today. All of these should be delivered tomorrow. How many packages should be delivered tomorrow?"""
    yesterday_packages = 80
    today_packages = 2 * yesterday_packages
    total_packages = yesterday_packages + today_packages
    result = total_packages
    return result

print(solution())