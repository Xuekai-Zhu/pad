def solution():
    # Calculate the total number of gates on every 3rd floor
    num_gates = 12 // 3

    # Calculate the total time spent showing ID at the gates
    id_time = num_gates * 2

    # Calculate the total distance to drive
    total_distance = 800 * 11

    # Calculate the total time to drive
    drive_time = total_distance / 10

    # Calculate the total time to get from top to bottom
    total_time = id_time + drive_time
    result = total_time
    return result

print(solution())