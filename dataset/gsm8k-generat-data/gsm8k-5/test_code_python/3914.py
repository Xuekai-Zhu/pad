def solution():
    warmup_time = 10  # Tony spent 10 minutes on the warm-up puzzle
    puzzle_time = 3 * warmup_time  # Each difficult puzzle took 3 times as long as the warm-up puzzle
    total_time = warmup_time + (2 * puzzle_time)  # Tony did two difficult puzzles

    result = total_time
    return result

print(solution())