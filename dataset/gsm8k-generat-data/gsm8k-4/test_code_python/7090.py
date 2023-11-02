def solution():
    """Stacy, Steve and Sylar have 1100 berries total. Stacy has 4 times as many berries as Steve, and Steve has double the number of berries that Skylar has. How many berries does Stacy have?"""
    # Define the total number of berries
    total_berries = 1100

    # Let's call the number of berries Skylar has 'x'
    x = total_berries / 7

    # Steve has double the number of berries that Skylar has
    steve = 2 * x

    # Stacy has 4 times as many berries as Steve
    stacy = 4 * steve

    result = stacy
    return result

print(solution())