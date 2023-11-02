def solution():
    # Define the time it took to solve the warm-up puzzle
    warm_up_puzzle_time = 10

    # Define the time it took to solve each of the more difficult puzzles
    difficult_puzzle1_time = 3 * warm_up_puzzle_time
    difficult_puzzle2_time = 3 * warm_up_puzzle_time

    # Calculate the total time spent on puzzles
    total_time = warm_up_puzzle_time + difficult_puzzle1_time + difficult_puzzle2_time
    result = total_time
    return result

print(solution())