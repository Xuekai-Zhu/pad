def solution():
    # Calculate the total number of apartments in the 2 buildings
    total_apartments = 2 * 12 * 6  # 2 buildings, 12 floors in each building, 6 apartments on each floor
    # Calculate the total number of doors needed for all the apartments
    total_doors = total_apartments * 7  # each apartment needs 7 doors
    result = total_doors
    return result

print(solution())