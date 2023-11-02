def solution():
    """Diane bakes four trays with 25 gingerbreads in each tray and three trays with 20 gingerbreads in each tray. How many gingerbreads does Diane bake?"""
    gingerbread_per_tray_1 = 25
    gingerbread_per_tray_2 = 20
    trays_1 = 4
    trays_2 = 3
    total_gingerbreads = (gingerbread_per_tray_1 * trays_1) + (gingerbread_per_tray_2 * trays_2)
    result = total_gingerbreads
    return result

print(solution())