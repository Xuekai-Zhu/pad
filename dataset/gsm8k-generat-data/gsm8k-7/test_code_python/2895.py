def solution():
    distance = 480
    speed = 60
    lunch_break = 0.5
    bathroom_breaks = 2 * 0.25

    # Calculate the time it takes to drive without breaks
    drive_time = distance / speed

    # Calculate the total time including breaks
    total_time = drive_time + lunch_break + bathroom_breaks

    result = total_time
    return result

print(solution())