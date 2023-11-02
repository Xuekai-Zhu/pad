def solution():
    # Define the number of moves and the average time per move for each player
    total_moves = 30
    polly_time_per_move = 28
    peter_time_per_move = 40

    # Calculate the total time for each player and for the entire match
    polly_total_time = polly_time_per_move * total_moves
    peter_total_time = peter_time_per_move * total_moves
    total_time = polly_total_time + peter_total_time

    # Convert the total time to minutes
    total_time_in_minutes = total_time / 60
    result = total_time_in_minutes
    return result

print(solution())