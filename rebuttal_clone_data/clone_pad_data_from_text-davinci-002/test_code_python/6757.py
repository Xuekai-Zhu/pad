def solution():
    total_awarded_damages = 80000
    punitive_damages = 3 * (50000 + 200000)
    total_damages = 50000 + 200000 + punitive_damages
    result = total_awarded_damages * (total_damages / 100)
    return result

print(solution())