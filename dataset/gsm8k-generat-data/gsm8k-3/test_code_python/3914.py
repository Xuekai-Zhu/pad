def solution():
    """Tony loved to solve difficult pen and paper puzzles.  He did a warm-up puzzle that only took 10 minutes and after that he did 2 puzzles that each took 3 times as long.  How long did he spend solving puzzles?"""
    # Define the time it took to complete the warm-up puzzle and the multiplier for the other puzzles
    WARMUP_TIME = 10
    MULTIPLIER = 3

    # Calculate the time it took to complete each of the other two puzzles
    puzzle1_time = WARMUP_TIME * MULTIPLIER
    puzzle2_time = WARMUP_TIME * MULTIPLIER

    # Calculate the total time spent solving puzzles
    total_time = WARMUP_TIME + puzzle1_time + puzzle2_time

    # Display the total time
    result = total_time
    return result

print(solution())