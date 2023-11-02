def solution():
    # Find out how many stuffies Jean keeps
    kept_stuffies = 60 / 3

    # Find out how many stuffies Jean gives away
    given_away_stuffies = 60 - kept_stuffies

    # Find out how many stuffies Janet gets
    janet_stuffies = given_away_stuffies / 4
    result = janet_stuffies
    return result

print(solution())