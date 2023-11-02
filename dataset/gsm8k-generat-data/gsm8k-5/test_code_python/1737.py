def solution():
    jerry_time = 3  # Jerry was in the pool for 3 minutes
    elaine_time = jerry_time * 2  # Elaine stayed in the pool for twice as long as Jerry
    george_time = elaine_time / 3  # George stayed in the pool for one-third as long as Elaine
    kramer_time = 0  # Kramer did not jump into the pool

    # Calculate the total time Jerry and his friends spent in the cold water
    total_time = jerry_time + elaine_time + george_time + kramer_time
    result = total_time
    return result

print(solution())