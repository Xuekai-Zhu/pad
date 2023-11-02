def solution():
    light_bulbs = 40
    used = 16
    given_away = (light_bulbs - used) / 2
    light_bulbs_left = light_bulbs - used - given_away
    result = light_bulbs_left
    return result

print(solution())