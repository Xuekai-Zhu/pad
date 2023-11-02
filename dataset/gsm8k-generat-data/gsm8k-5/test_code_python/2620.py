def solution():
    starting_tokens = 36  # Ryan started with 36 tokens
    pac_man_tokens = starting_tokens / 3  # Ryan spent a third of his tokens on Pac-Man
    candy_crush_tokens = starting_tokens / 4  # Ryan spent a fourth of his tokens on Candy Crush
    ski_ball_tokens = 7  # Ryan spent 7 tokens on Ski-ball
    tokens_from_parents = 7 * ski_ball_tokens  # Ryan's parents bought him seven times as many tokens as he spent on Ski-ball

    # Calculate the total number of tokens Ryan has left
    total_tokens = starting_tokens - pac_man_tokens - candy_crush_tokens - ski_ball_tokens + tokens_from_parents
    result = total_tokens
    return result

print(solution())