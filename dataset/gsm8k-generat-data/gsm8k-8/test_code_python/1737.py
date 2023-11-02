def solution():
    # Define time lengths in minutes
    jerry_time = 3
    elaine_time = jerry_time * 2
    george_time = elaine_time / 3
    kramer_time = 0

    # Calculate total time in minutes
    total_time = jerry_time + elaine_time + george_time + kramer_time
    result = total_time
    return result

print(solution())