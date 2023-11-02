def solution():
    afternoon_soccer_camp = 750 # given
    morning_soccer_camp = 0.25 * 0.5 * afternoon_soccer_camp # 1/4 of kids going to soccer camp are going in the morning
    total_soccer_camp = afternoon_soccer_camp + morning_soccer_camp # total kids going to soccer camp
    total_kids = 2 * total_soccer_camp # since half the kids are going to soccer camp
    result = total_kids
    return result

print(solution())