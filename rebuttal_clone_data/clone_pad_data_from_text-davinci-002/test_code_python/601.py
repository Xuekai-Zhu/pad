def solution():
    cheetah_speed = 60
    gazelle_speed = 40
    distance = 210
    time = (distance / (cheetah_speed - gazelle_speed)) * 3600
    result = time
    return result

print(solution())