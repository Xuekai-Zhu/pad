def solution():
    """Charlie can make 5350 steps while running on a 3-kilometer running field. If he can run around the field 2 1/2 times during a running session, how many steps was he able to make?"""
    steps_per_kilometer = 5350 / 3
    laps = 2.5
    total_distance = 3 * laps
    total_steps = total_distance * steps_per_kilometer
    result = total_steps
    return result

print(solution())