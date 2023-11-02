def solution():
    # Calculate the total time the plane hovered in each time zone over two days
    mountain_time = 3 + 2  # 3 hours on the first day, 2 on the second
    central_time = 4 + 2  # 4 hours on the first day, 2 on the second
    eastern_time = 2 + 2  # 2 hours on the first day, 2 on the second

    # Calculate the total time the plane hovered overall
    total_time = mountain_time + central_time + eastern_time

    result = total_time
    return result

print(solution())