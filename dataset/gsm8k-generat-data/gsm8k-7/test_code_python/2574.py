def solution():
    yvonne_laps = 10
    yvonne_time = 5  # minutes

    sister_laps = yvonne_laps / 2
    sister_time = yvonne_time

    joel_laps = sister_laps * 3
    joel_time = sister_time

    # Calculate Joel's laps per minute
    joel_laps_per_minute = joel_laps / joel_time

    result = joel_laps
    return result

print(solution())