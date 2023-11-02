def solution():
    pieces_per_day = 40
    time_per_day = 10

    # Calculate how long it would take Moe to eat 1 piece of cuttlebone
    time_per_piece = time_per_day / pieces_per_day

    # Calculate how long it would take Moe to eat 800 pieces of cuttlebone
    time_for_800_pieces = time_per_piece * 800
    result = time_for_800_pieces
    return result

print(solution())