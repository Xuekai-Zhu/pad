def solution():
    """Nathan went to the arcade. He played the air hockey game 2 times and the basketball game 4 times. If each game cost 3 tokens, how many tokens did he use?"""
    air_hockey_games = 2
    basketball_games = 4
    tokens_per_game = 3
    total_tokens = (air_hockey_games + basketball_games) * tokens_per_game
    result = total_tokens
    return result

print(solution())