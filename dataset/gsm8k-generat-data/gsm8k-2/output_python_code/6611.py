def solution():
    """Camila has only gone hiking 7 times in her life. Amanda has gone on 8 times as many hikes as Camila, and Steven has gone on 15 more hikes than Amanda. If Camila wants to say that she has hiked as many times as Steven and plans to go on 4 hikes a week, how many weeks would it take Camila to achieve her goal?"""
    camila_hikes = 7
    amanda_hikes = 8 * camila_hikes
    steven_hikes = amanda_hikes + 15
    weeks_to_equal = (steven_hikes - camila_hikes) / 4
    result = weeks_to_equal
    return result

print(solution())