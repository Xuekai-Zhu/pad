def solution():
    pieces_per_day = 40  # Moe eats 40 pieces every day
    time_per_day = 10  # It takes 10 seconds for Moe to eat 40 pieces

    # Calculate the time it takes for Moe to eat 1 piece
    time_per_piece = time_per_day / pieces_per_day

    # Calculate the total time it would take for Moe to eat 800 pieces
    total_time = time_per_piece * 800
    result = total_time
    return result

print(solution())