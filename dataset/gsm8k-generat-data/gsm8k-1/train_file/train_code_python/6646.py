def solution():
    """Yesterday, Sarah collected 50 aluminum cans while Lara collected 30 more aluminum cans. Today, Sarah collected 40 while Lara collected 70 aluminum cans. How many fewer cans did they collect today than yesterday?"""
    sarah_yesterday = 50
    lara_yesterday = sarah_yesterday + 30
    sarah_today = 40
    lara_today = 70
    cans_yesterday = sarah_yesterday + lara_yesterday
    cans_today = sarah_today + lara_today
    difference = cans_yesterday - cans_today
    result = difference
    return result

print(solution())