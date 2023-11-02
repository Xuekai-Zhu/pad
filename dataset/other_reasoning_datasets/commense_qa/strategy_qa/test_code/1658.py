def solution():
    knows_physics = True
    knows_astrology = False
    if knows_physics and not knows_astrology:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())