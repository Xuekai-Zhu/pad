def solution():
    # total number of peanut butter cookies
    pb_cookies = 40 + 30

    # total number of cookies
    total_cookies = pb_cookies + 50 + 20

    # probability of Renee picking a peanut butter cookie
    pb_prob = pb_cookies / total_cookies

    # probability of Renee having an allergic reaction
    reaction_prob = pb_prob * 100

    result = reaction_prob
    return result

print(solution())