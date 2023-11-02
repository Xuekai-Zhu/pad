def solution():
    """Jenny brought in 40 peanut butter cookies and 50 chocolate chip cookies for the bake sale. Marcus brought in 30 peanut butter cookies and and 20 lemon cookies.
    If Renee, who's allergic to peanuts, picks a cookie at random, what is the chance she'll have an allergic reaction expressed as a percentage?"""
    pb_cookies = 40 + 30
    total_cookies = pb_cookies + 50 + 20
    allergic_reaction_chance = (pb_cookies / total_cookies) * 100
    result = allergic_reaction_chance
    return result

print(solution())