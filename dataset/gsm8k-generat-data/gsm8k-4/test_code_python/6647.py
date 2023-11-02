def solution():
    """Yesterday, Sarah collected 50 aluminum cans while Lara collected 30 more aluminum cans. Today, Sarah collected 40 while Lara collected 70 aluminum cans. How many fewer cans did they collect today than yesterday?"""
    # Calculate the number of cans collected yesterday
    sarah_yesterday = 50
    lara_yesterday = sarah_yesterday + 30
    total_yesterday = sarah_yesterday + lara_yesterday

    # Calculate the number of cans collected today
    sarah_today = 40
    lara_today = 70
    total_today = sarah_today + lara_today

    # Calculate the difference in the number of cans collected
    difference = total_yesterday - total_today

    # return the result
    result = difference
    return result

print(solution())