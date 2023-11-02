def solution():
    # Calculate the time it takes Jerry to run to school and back
    jerry_time = 2 * 15  # 15 minutes for one-way trip, times 2 for round trip

    # Calculate the speed that Jerry runs to school and back
    jerry_speed = 4 / (jerry_time / 60)  # Convert time to minutes, then divide distance

    # Calculate the time it takes Carson to run to school
    carson_time = jerry_time / 2  # Since Jerry can do round trip in same time, Carson takes half that time

    # Calculate the speed that Carson runs
    carson_speed = 4 / (carson_time / 60)  # Convert time to minutes, then divide distance

    result = carson_speed
    return result

print(solution())