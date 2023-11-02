def solution():
    hikes_camila = 7  # Camila has gone hiking 7 times
    hikes_amanda = 8 * hikes_camila  # Amanda has gone on 8 times as many hikes as Camila
    hikes_steven = hikes_amanda + 15  # Steven has gone on 15 more hikes than Amanda
    hikes_goal = hikes_steven  # Camila wants to say that she has hiked as many times as Steven
    hikes_remaining = hikes_goal - hikes_camila  # Number of hikes remaining for Camila to achieve her goal
    weeks = hikes_remaining / 4  # Camila plans to go on 4 hikes a week

    result = weeks
    return result

print(solution())