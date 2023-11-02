def solution():
    """Tony loved to solve difficult pen and paper puzzles. He did a warm-up puzzle that only took 10 minutes and after that he did 2 puzzles that each took 3 times as long. How long did he spend solving puzzles?"""
    warmup_time = 10
    puzzle_time = 3*warmup_time
    total_puzzle_time = 2*puzzle_time
    total_time = warmup_time + total_puzzle_time
    result = total_time
    return result

print(solution())