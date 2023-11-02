def solution():
    """Charlie can make 5350 steps while running on a 3-kilometer running field. If he can run around the field 2 1/2 times during a running session, how many steps was he able to make?"""
    # Define the distance of the running field
    field_distance = 3

    # Calculate the total distance Charlie ran during the session
    total_distance = field_distance * 2.5

    # Calculate the number of steps taken per kilometer
    steps_per_kilometer = 5350 / 3

    # Calculate the total number of steps taken during the session
    total_steps = steps_per_kilometer * total_distance

    result = total_steps
    return result

print(solution())