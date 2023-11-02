def solution():
    """Yanna baked twenty butter cookies and forty biscuits in the morning. In the afternoon, she baked ten butter cookies and twenty biscuits. How many more biscuits did she bake than butter cookies?"""
    morning_butter_cookies = 20
    morning_biscuits = 40
    afternoon_butter_cookies = 10
    afternoon_biscuits = 20
    total_butter_cookies = morning_butter_cookies + afternoon_butter_cookies
    total_biscuits = morning_biscuits + afternoon_biscuits
    difference = total_biscuits - total_butter_cookies
    result = difference
    return result

print(solution())