def solution():
    # Calculate the total number of game tokens needed for all friends to play
    total_tokens = 60 * 2 * 4  # each friend plays 60 games, each game costs 2 tokens, there are 4 friends

    # Calculate the cost in dollars
    cost_in_dollars = total_tokens / 30  # 30 tokens cost $1

    result = cost_in_dollars
    return result

print(solution())