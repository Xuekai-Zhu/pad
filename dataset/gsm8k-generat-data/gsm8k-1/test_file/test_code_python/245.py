def solution():
    """On Monday, Sue ate 4 times as many cookies as her sister. On Tuesday, she ate twice as many cookies as her sister. Her sister ate 5 cookies on Monday and 13 the next day. If 1 cookie has 200 calories, how many more calories did Sue consume than her sister?"""
    s_monday = 4 * 5  # Sue ate 4 times as many as her sister, who ate 5 cookies on Monday
    s_tuesday = 2 * 13  # Sue ate twice as many as her sister, who ate 13 cookies on Tuesday
    s_total = s_monday + s_tuesday  # calculate total number of cookies Sue ate
    s_calories = s_total * 200  # calculate total calories Sue consumed
    sister_calories = (5 + 13) * 200  # calculate total calories sister consumed
    calorie_diff = s_calories - sister_calories  # calculate difference in calories
    result = calorie_diff
    return result

print(solution())