def solution():
    # Original number of pens in the jar
    blue_pens = 9
    black_pens = 21
    red_pens = 6

    # Pens removed from the jar
    blue_pens_removed = 4
    black_pens_removed = 7

    # New number of pens in the jar
    blue_pens_remaining = blue_pens - blue_pens_removed
    black_pens_remaining = black_pens - black_pens_removed
    red_pens_remaining = red_pens

    # Total number of pens remaining in the jar
    total_pens_remaining = blue_pens_remaining + black_pens_remaining + red_pens_remaining
    result = total_pens_remaining
    return result

print(solution())