def solution():
    pogs_release_year = 1990
    surfing_popularity_years = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
    if pogs_release_year in surfing_popularity_years:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())