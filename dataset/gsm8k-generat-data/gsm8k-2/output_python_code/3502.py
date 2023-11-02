def solution():
    """It takes Derek 9 minutes to walk a mile if he doesn't have to walk with his brother. If he has to take his brother it takes 12 minutes to walk a mile. How many minutes longer would it take him to walk 20 miles if he had to take his brother?"""
    miles = 20
    solo_time = 9 * miles
    duo_time = 12 * miles
    difference = duo_time - solo_time
    result = difference
    return result

print(solution())