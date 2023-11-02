def solution():
    """Ben's hockey team is 60% boys and the rest are girls. Half the girls are juniors and the other half are seniors. 
    If the team has 50 players, how many junior girls are there?"""
    total_players = 50
    boys_percentage = 60
    girls_percentage = 100 - boys_percentage
    girls_total = (girls_percentage / 100) * total_players
    junior_girls = girls_total / 2
    result = junior_girls
    return result

print(solution())