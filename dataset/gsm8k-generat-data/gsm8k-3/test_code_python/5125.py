def solution():
    """Jonathan ran 7.5 kilometers. Mercedes ran twice that distance and Davonte ran 2 kilometers farther than Mercedes. How many kilometers did Mercedes and Davonte run in total?"""
    # Calculate Mercedes' distance
    mercedes_distance = 2 * 7.5

    # Calculate Davonte's distance
    davonte_distance = mercedes_distance + 2

    # Calculate the total distance run
    total_distance = mercedes_distance + davonte_distance

    # Display the total distance run
    result = total_distance
    return result

print(solution())