def solution():
    # Calculate the number of math problems Marvin practiced today
    solved_yesterday = 40
    practiced_today = 3 * solved_yesterday

    # Calculate the number of math problems Arvin practiced each day
    practiced_arvin = 2 * practiced_today

    # Calculate the total number of math problems they have practiced altogether
    total_practiced = solved_yesterday + practiced_today + practiced_arvin

    result = total_practiced
    return result

print(solution())