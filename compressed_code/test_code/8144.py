def solution():
    
    total_stuffies = 60
    kept_stuffies = total_stuffies // 3
    given_stuffies = total_stuffies - kept_stuffies
    janet_stuffies = given_stuffies // 4
    result = janet_stuffies
    return result

print(solution())