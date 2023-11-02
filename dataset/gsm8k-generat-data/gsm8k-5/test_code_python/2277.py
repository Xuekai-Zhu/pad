def solution():
    days_in_week = 7  # Number of days in a week
    total_friends = 2 * days_in_week  # Davante has twice as many friends as there are days in the week

    # Calculate the number of boys among Davante's friends
    boys_friends = total_friends - 3  # 3 of his friends are girls

    result = boys_friends
    return result

print(solution())