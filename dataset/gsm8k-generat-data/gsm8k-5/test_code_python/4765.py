def solution():
    outlining_time = 30  # Javier spends 30 minutes outlining his speech
    writing_time = outlining_time + 28  # Javier spends 28 more minutes writing than outlining
    practicing_time = writing_time / 2  # Javier spends half as much time practicing as writing

    # Calculate the total time Javier spends on his speech
    total_time = outlining_time + writing_time + practicing_time
    result = total_time
    return result

print(solution())