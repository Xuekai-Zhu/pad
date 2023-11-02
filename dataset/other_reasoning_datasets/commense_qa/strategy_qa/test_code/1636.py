def solution():
    little_women_published_year = 1868
    civil_war_ended_year = 1865
    if little_women_published_year > civil_war_ended_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())