def solution():
    num_trays_1 = 4
    num_gingerbreads_1 = 25

    num_trays_2 = 3
    num_gingerbreads_2 = 20

    # Calculate the total number of gingerbreads in the first type of tray
    total_gingerbreads_1 = num_trays_1 * num_gingerbreads_1

    # Calculate the total number of gingerbreads in the second type of tray
    total_gingerbreads_2 = num_trays_2 * num_gingerbreads_2

    # Calculate the total number of gingerbreads baked
    total_gingerbreads = total_gingerbreads_1 + total_gingerbreads_2
    result = total_gingerbreads
    return result

print(solution())