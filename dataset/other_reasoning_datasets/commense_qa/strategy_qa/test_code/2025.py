def solution():
    max_windsurfing_speed = 100
    hurricane_speed = 175
    if max_windsurfing_speed < hurricane_speed:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())