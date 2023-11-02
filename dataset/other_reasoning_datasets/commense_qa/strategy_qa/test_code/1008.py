def solution():
    acela_max_speed = 150 #mph
    sound_speed = 770 #mph
    if acela_max_speed < sound_speed:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())