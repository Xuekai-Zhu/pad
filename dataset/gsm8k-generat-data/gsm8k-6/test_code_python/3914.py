def solution():
    # Calculate the total time Tony spent solving puzzles
    warmup_time = 10  # minutes
    puzzle_time = 3 * warmup_time  # each puzzle took 3 times as long as the warm-up puzzle
    total_time = warmup_time + 2*puzzle_time  # Tony did 2 more puzzles that each took 3 times as long as the warm-up puzzle
    result = total_time  # minutes
    return result

print(solution())