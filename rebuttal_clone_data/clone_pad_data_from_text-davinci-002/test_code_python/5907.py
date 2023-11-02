def solution():
    total_peanut_butter_cookies = 40 + 30
    total_cookies = total_peanut_butter_cookies + 50 + 20
    allergic_reaction_cookies = total_peanut_butter_cookies
    non_allergic_reaction_cookies = total_cookies - allergic_reaction_cookies
    percent_chance_of_allergic_reaction = (allergic_reaction_cookies / total_cookies) * 100
    result = percent_chance_of_allergic_reaction
    return result

print(solution())