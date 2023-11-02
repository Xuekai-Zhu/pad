def solution():
    # Calculate the total number of gingerbreads baked on four trays with 25 gingerbreads each
    total_gingerbreads_25 = 4 * 25

    # Calculate the total number of gingerbreads baked on three trays with 20 gingerbreads each
    total_gingerbreads_20 = 3 * 20

    # Add the total number of gingerbreads baked on both types of trays
    total_gingerbreads = total_gingerbreads_25 + total_gingerbreads_20
    result = total_gingerbreads
    return result

print(solution())