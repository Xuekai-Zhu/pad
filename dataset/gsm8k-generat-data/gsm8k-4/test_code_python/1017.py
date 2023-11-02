def solution():
    """Stacy has 2 more than triple as many berries as Steve. Steve has one half as many berries as Skylar. If Skylar has 20 berries, how many berries does Stacy have?"""
    # Define the number of berries Skylar has
    skylar = 20

    # Calculate the number of berries Steve has
    steve = skylar / 2

    # Calculate the number of berries Stacy has
    stacy = 3 * steve + 2

    # Return the result
    result = stacy
    return result

print(solution())