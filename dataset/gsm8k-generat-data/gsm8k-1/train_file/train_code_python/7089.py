def solution():
    """Stacy, Steve and Sylar have 1100 berries total. Stacy has 4 times as many berries as Steve, and Steve has double the number of berries that Skylar has. How many berries does Stacy have?"""
    total_beries = 1100
    # Let's assume the number of berries Skylar has is x
    # Then, Steve has 2x berries
    # And, Stacy has 4(2x) berries = 8x berries
    x = total_beries / (1 + 2 + 4)
    stacy_beries = 8 * x
    result = stacy_beries
    return result

print(solution())