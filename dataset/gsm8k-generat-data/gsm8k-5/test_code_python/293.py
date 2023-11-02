def solution():
    stage_time = 6  # Carlotta's final stage performance is 6 minutes long
    practice_time = 3 * stage_time  # Carlotta spends 3 minutes practicing for every 1 minute on stage
    tantrum_time = 5 * stage_time  # Carlotta spends 5 minutes throwing tantrums for every 1 minute on stage

    # Calculate the total combined amount of time Carlotta spends on practicing, throwing tantrums, and singing
    total_time = stage_time + practice_time + tantrum_time
    result = total_time
    return result

print(solution())