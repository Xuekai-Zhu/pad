def solution():
    """Jenny brought in 40 peanut butter cookies and 50 chocolate chip cookies for the bake sale. Marcus brought in 30 peanut butter cookies and and 20 lemon cookies. If Renee, who's allergic to peanuts, picks a cookie at random, what is the chance she'll have an allergic reaction expressed as a percentage?"""
    num_peanut_butter = 40 + 30
    num_total_cookies = num_peanut_butter + 50 + 20
    fraction_allergic = num_peanut_butter / num_total_cookies
    percent_allergic = fraction_allergic * 100
    result = percent_allergic
    return result

print(solution())