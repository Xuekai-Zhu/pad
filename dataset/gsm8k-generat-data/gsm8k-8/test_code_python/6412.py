def solution():
    # Calculate the number of gingerbreads in the four trays of 25
    tray1 = 25
    tray2 = 25
    tray3 = 25
    tray4 = 25
    total_in_25_trays = tray1 + tray2 + tray3 + tray4

    # Calculate the number of gingerbreads in the three trays of 20
    tray5 = 20
    tray6 = 20
    tray7 = 20
    total_in_20_trays = tray5 + tray6 + tray7

    # Calculate the total number of gingerbreads Diane baked
    total_gingerbreads = total_in_25_trays + total_in_20_trays
    result = total_gingerbreads
    return result

print(solution())