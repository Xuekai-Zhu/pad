def solution():
    """Stacy, Steve and Sylar have 1100 berries total. Stacy has 4 times as many berries as Steve, and Steve has double the number of berries that Skylar has. How many berries does Stacy have?"""
    total_Berries = 1100
    Sylar_Berries = total_Berries / 7
    Steve_Berries = Sylar_Berries * 2
    Stacy_Berries = Steve_Berries * 4
    result = Stacy_Berries
    return result

print(solution())