def solution():
    olympic_standard_men = 259 #in seconds (4 minutes and 19 seconds)
    olympic_standard_women = 280 #in seconds (4 minutes and 40 seconds)
    athlete_time = 240 #in seconds (assuming the athlete runs the mile in 4 minutes)
    if athlete_time > olympic_standard_men or athlete_time > olympic_standard_women:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())