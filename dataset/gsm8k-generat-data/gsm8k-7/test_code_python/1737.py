def solution():
    jerry_time = 3
    elaine_time = jerry_time * 2
    george_time = elaine_time / 3
    kramer_time = 0  # Kramer did not participate

    # Calculate the combined total of minutes that Jerry and his friends were in the cold water
    total_time = jerry_time + elaine_time + george_time + kramer_time
    result = total_time
    return result

print(solution())