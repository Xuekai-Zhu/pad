def solution():
    """It takes Derek 9 minutes to walk a mile if he doesn't have to walk with his brother. If he has to take his brother it takes 12 minutes to walk a mile. How many minutes longer would it take him to walk 20 miles if he had to take his brother?"""
    miles = 20
    without_brother = 9 * miles
    with_brother = 12 * miles
    time_difference = with_brother - without_brother
    result = time_difference
    return result

print(solution())