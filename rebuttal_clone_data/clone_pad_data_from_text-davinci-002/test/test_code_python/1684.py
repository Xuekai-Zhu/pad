def solution():
    total_stuffies = 60
    kept_stuffies = total_stuffies / 3
    given_away = total_stuffies - kept_stuffies
    given_to_sister = given_away / 4
    result = given_to_sister
    return result

print(solution())