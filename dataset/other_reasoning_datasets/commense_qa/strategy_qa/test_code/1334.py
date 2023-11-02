def solution():
    nine_inch_nails_genre = "industrial heavy rock"
    aretha_franklin_genre = "soul and R&B"
    aretha_franklin_influence = "gospel choir"
    nine_inch_nails_lyrics = "profane and anti-God"
    if nine_inch_nails_lyrics not in aretha_franklin_influence:
        result = "no"
    else:
        result = "cannot be determined"
    return result

print(solution())