def solution():
    """Camila has only gone hiking 7 times in her life. Amanda has gone on 8 times as many hikes as Camila, and Steven has gone on 15 more hikes than Amanda. If Camila wants to say that she has hiked as many times as Steven and plans to go on 4 hikes a week, how many weeks would it take Camila to achieve her goal?"""
    # Define the number of hikes for Camila, Amanda, and Steven
    camila_hikes = 7
    amanda_hikes = 8 * camila_hikes
    steven_hikes = amanda_hikes + 15

    # Calculate the number of hikes Camila needs to go on to catch up with Steven
    hikes_needed = steven_hikes - camila_hikes

    # Calculate the number of weeks it will take Camila to achieve her goal
    weeks_needed = hikes_needed / 4

    # Display the number of weeks needed
    result = weeks_needed
    return result

print(solution())