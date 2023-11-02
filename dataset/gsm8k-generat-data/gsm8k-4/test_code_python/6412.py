def solution():
    """Diane bakes four trays with 25 gingerbreads in each tray and three trays with 20 gingerbreads in each tray. How many gingerbreads does Diane bake?"""
    # Define the number of gingerbreads in each tray
    gingerbreads_per_tray_1 = 25
    gingerbreads_per_tray_2 = 20

    # Calculate the total number of gingerbreads baked in the first type of tray
    total_gingerbreads_1 = gingerbreads_per_tray_1 * 4

    # Calculate the total number of gingerbreads baked in the second type of tray
    total_gingerbreads_2 = gingerbreads_per_tray_2 * 3

    # Calculate the total number of gingerbreads baked
    total_gingerbreads = total_gingerbreads_1 + total_gingerbreads_2

    # return the result
    result = total_gingerbreads
    return result

print(solution())