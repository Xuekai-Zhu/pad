def solution():
    """Biff and Kenneth decide to compete in a 500-yard rowboat race. If Biff rows at a speed of 50 yards per minute and Kenneth rows at a speed of 51 yards per minute,
    how many yards past the finish line will Kenneth be when Biff crosses the finish line?"""
    distance = 500
    biff_speed = 50
    kenneth_speed = 51
    biff_time = distance / biff_speed
    kenneth_time = distance / kenneth_speed
    kenneth_distance = kenneth_speed * (biff_time + kenneth_time)
    excess_distance = kenneth_distance - distance
    result = excess_distance
    return result

print(solution())