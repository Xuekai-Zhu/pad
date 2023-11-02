def solution():
    """Ryan started with 36 tokens at the arcade. Ryan wasted a third of his tokens on Pac-Man, a fourth of his tokens on Candy Crush, and 7 on Ski-ball. Then, his parents bought him seven times as many tokens as he spent on Ski-ball. How many tokens did Ryan end up with?"""
    starting_tokens = 36
    pac_man_tokens = starting_tokens // 3
    candy_crush_tokens = starting_tokens // 4
    ski_ball_tokens = 7
    spent_tokens = pac_man_tokens + candy_crush_tokens + ski_ball_tokens
    parents_bought_tokens = 7 * ski_ball_tokens
    ending_tokens = starting_tokens - spent_tokens + parents_bought_tokens
    result = ending_tokens
    return result

print(solution())