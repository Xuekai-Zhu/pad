def solution():
    num_groups = 9
    num_repeated_players = 3  # Two in one group and one in another

    # Calculate the total number of unique players Mona grouped with
    total_unique_players = (num_groups * 4) - num_repeated_players

    result = total_unique_players
    return result

print(solution())