def solution():
    """Charlie can make 5350 steps while running on a 3-kilometer running field. If he can run around the field 2 1/2 times during a running session, how many steps was he able to make?"""
    # Define the number of steps Charlie can make per kilometer
    STEPS_PER_KM = 5350 / 3

    # Define the number of times Charlie runs around the field
    lap_count = 2.5

    # Calculate the total distance Charlie runs
    total_distance = lap_count * 3

    # Calculate the total number of steps Charlie makes
    total_steps = total_distance * STEPS_PER_KM

    # Display the total number of steps Charlie makes
    result = total_steps
    return result

print(solution())