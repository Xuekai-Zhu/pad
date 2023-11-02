def solution():
    """Diane bakes four trays with 25 gingerbreads in each tray and three trays with 20 gingerbreads in each tray. How many gingerbreads does Diane bake?"""
    # Define the number of gingerbreads in each tray
    GINGERBREADS_1 = 25
    GINGERBREADS_2 = 20

    # Define the number of trays for each type of gingerbread
    TRAYS_1 = 4
    TRAYS_2 = 3

    # Calculate the total number of gingerbreads baked
    total_gingerbreads = (GINGERBREADS_1 * TRAYS_1) + (GINGERBREADS_2 * TRAYS_2)

    # Display the total number of gingerbreads baked
    result = total_gingerbreads
    return result

print(solution())