def solution():
    crane1_height = 228
    building1_height = 200

    crane2_height = 120
    building2_height = 100

    crane3_height = 147
    building3_height = 140

    # Calculate the difference in height between the cranes and their respective buildings
    diff1 = crane1_height - building1_height
    diff2 = crane2_height - building2_height
    diff3 = crane3_height - building3_height

    # Calculate the average difference as a percentage
    avg_diff_percent = ((diff1/building1_height) + (diff2/building2_height) + (diff3/building3_height)) / 3 * 100

    result = avg_diff_percent
    return result

print(solution())