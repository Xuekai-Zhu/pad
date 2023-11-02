def solution():
    """Ben's hockey team is 60% boys and the rest are girls. Half the girls are juniors and the other half are seniors. If the team has 50 players, how many junior girls are there?"""
    total_players = 50
    boys_ratio = 0.6
    girls_ratio = 1 - boys_ratio
    girls_count = int(girls_ratio * total_players)
    junior_girls_count = int(girls_count / 2)
    result = junior_girls_count
    return result

print(solution())