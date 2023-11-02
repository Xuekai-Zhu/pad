def solution():
    """Camila has only gone hiking 7 times in her life. Amanda has gone on 8 times as many hikes as Camila, and Steven has gone on 15 more hikes than Amanda. If Camila wants to say that she has hiked as many times as Steven and plans to go on 4 hikes a week, how many weeks would it take Camila to achieve her goal?"""
    # Calculate the number of hikes Camila has to do to catch up with Steven
    camila_hikes = 15 + 8 * 7 - 7

    # Calculate the number of weeks it will take Camila to achieve her goal
    weeks = camila_hikes / 4

    # round up the number of weeks to ensure Camila has achieved her goal
    result = math.ceil(weeks)
    return result

print(solution())