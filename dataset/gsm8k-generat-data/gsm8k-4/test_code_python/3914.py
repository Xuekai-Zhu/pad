def solution():
    """Tony loved to solve difficult pen and paper puzzles. He did a warm-up puzzle that only took 10 minutes and after that he did 2 puzzles that each took 3 times as long. How long did he spend solving puzzles?"""
    # Define the time it took to solve the warm-up puzzle
    warmup_time = 10

    # Define the time it took to solve each of the more difficult puzzles
    difficult_puzzle_time = warmup_time * 3

    # Calculate the total time it took to solve all the puzzles
    total_time = warmup_time + (2 * difficult_puzzle_time)

    # return the result
    result = total_time
    return result

print(solution())