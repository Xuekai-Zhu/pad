def solution():
    crane1_height = 228
    building1_height = 200
    crane2_height = 120
    building2_height = 100
    crane3_height = 147
    building3_height = 140

    # Calculate the percentage the first crane is taller than the building
    percent1 = ((crane1_height - building1_height) / building1_height) * 100

    # Calculate the percentage the second crane is taller than the building
    percent2 = ((crane2_height - building2_height) / building2_height) * 100

    # Calculate the percentage the third crane is taller than the building
    percent3 = ((crane3_height - building3_height) / building3_height) * 100

    # Calculate the average percentage taller the cranes are than the buildings
    average_percent = (percent1 + percent2 + percent3) / 3
    result = average_percent
    return result

print(solution())