def solution():
    """Dylan attended a wedding where there were 100 guests in the reception. Each guest brought a plate of 15 cookies. The bride decided to give 1/2 of the cookies to the church next door as a thank you for helping in the wedding reception. If each person in the church next door got 15 cookies, how many people were in the church next door?"""
    total_cookies = 100 * 15
    cookies_given_away = total_cookies / 2
    people_in_church = cookies_given_away / 15
    result = people_in_church
    return result

print(solution())