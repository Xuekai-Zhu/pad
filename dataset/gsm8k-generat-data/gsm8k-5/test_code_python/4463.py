def solution():
    first_player = 78  # The first player eats 78 seeds
    second_player = 53  # The second player eats 53 seeds
    third_player = second_player + 30  # The third player eats 30 more seeds than the second

    # Calculate the total number of seeds eaten
    total_seeds = first_player + second_player + third_player
    result = total_seeds
    return result

print(solution())