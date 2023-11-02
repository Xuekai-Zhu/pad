def solution():
    num_times_played_mark = 10
    num_times_won_mark = 1

    num_times_played_jill = num_times_played_mark * 2
    num_times_won_jill = num_times_played_jill * 0.75

    # Calculate the total number of times Jenny has won games with her friends
    total_wins = num_times_won_mark + num_times_won_jill

    result = total_wins
    return result

print(solution())