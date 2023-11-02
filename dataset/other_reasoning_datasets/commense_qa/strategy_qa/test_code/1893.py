def solution():
    beatles_active_years = range(1960, 1970)
    disco_year = 1972
    if max(beatles_active_years) < disco_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())