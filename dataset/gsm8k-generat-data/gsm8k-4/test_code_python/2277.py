def solution():
    """Davante has twice as many friends as there are days in the week. 3 of his friends are girls. How many friends does he have that are boys?"""
    # Define the number of days in a week
    days_in_week = 7

    # Calculate the total number of friends Davante has
    total_friends = days_in_week * 2

    # Calculate the number of friends that are boys
    boys_friends = total_friends - 3

    # return the result
    result = boys_friends
    return result

print(solution())