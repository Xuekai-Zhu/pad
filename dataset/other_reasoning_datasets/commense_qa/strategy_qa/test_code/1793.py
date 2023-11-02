def solution():
    gerald_ford_affiliation = "Republican"
    nancy_pelosi_affiliation = "Democratic"
    ford_conservative = True
    pelosi_medicare_medicaid_supporter = True
    if gerald_ford_affiliation != nancy_pelosi_affiliation and ford_conservative and pelosi_medicare_medicaid_supporter:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())