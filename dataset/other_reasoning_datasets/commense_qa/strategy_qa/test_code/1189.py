def solution():
    spider_wasp_pain_rating = 4
    bullet_ant_pain_rating = 4.5 #since it is higher than a rating of 4+
    if spider_wasp_pain_rating < bullet_ant_pain_rating: # lower rating means less pain
        result = "yes"
    else:
        result = "no"
    return result

print(solution())