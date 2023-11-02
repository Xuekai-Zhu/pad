def solution():
    # Calculate the number of buildings collapsed in each earthquake
    earthquake_1 = 4  # buildings collapsed in the first earthquake
    earthquake_2 = 2 * earthquake_1  # buildings collapsed in the second earthquake
    earthquake_3 = 2 * earthquake_2  # buildings collapsed in the third earthquake
    earthquake_4 = 2 * earthquake_3  # buildings collapsed in the fourth earthquake

    # Calculate the total number of buildings collapsed including those from the first earthquake
    total_buildings = earthquake_1 + earthquake_2 + earthquake_3 + earthquake_4
    result = total_buildings
    return result

print(solution())