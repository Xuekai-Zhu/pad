def solution():
    """Davante has twice as many friends as there are days in the week. 3 of his friends are girls. How many friends does he have that are boys?"""
    # Calculate the number of days in a week
    days_in_week = 7

    # Calculate the total number of friends Davante has
    total_friends = days_in_week * 2

    # Subtract the number of girl friends to get the number of boy friends
    boy_friends = total_friends - 3

    # Display the number of boy friends
    result = boy_friends
    return result

print(solution())