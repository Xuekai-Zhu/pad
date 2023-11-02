def solution():
    num_floors = 12
    id_floors = [i for i in range(3, num_floors+1, 3)]  # floors with ID gates
    gate_time = 2  # minutes to show ID
    drive_distance = 800  # feet
    drive_speed = 10  # feet per second

    # Calculate the time to get from one floor to the next
    drive_time = drive_distance / drive_speed

    # Calculate the total time to get to the bottom from the top
    total_time = 0
    for floor in range(num_floors, 0, -1):
        if floor in id_floors:
            total_time += gate_time  # add time for ID gate
        if floor != 1:
            total_time += drive_time  # add time for driving down
    result = total_time * 60  # convert to seconds
    return result

print(solution())