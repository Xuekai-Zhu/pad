def solution():
    """Stacy, Steve and Sylar have 1100 berries total. Stacy has 4 times as many berries as Steve, and Steve has double the number of berries that Skylar has. How many berries does Stacy have?"""
    # Define the total number of berries
    total = 1100

    # Calculate the number of berries that Skylar has
    sylar = total / 7

    # Calculate the number of berries that Steve has
    steve = sylar * 2

    # Calculate the number of berries that Stacy has
    stacy = steve * 4

    # Display the number of berries that Stacy has
    result = stacy
    return result

print(solution())