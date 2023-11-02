def solution():
    """Carolyn buys a silverware set with 6 knives, 12 forks, and three times as many spoons as knives. Then her friend trades her 10 knives for 6 spoons. What percentage of Carolyn's silverware is knives?"""
    knives = 6
    forks = 12
    spoons = 3 * knives
    knives_after_trade = knives + 10
    spoons_after_trade = spoons - (6 * (10/6))
    total_silverware = knives_after_trade + forks + spoons_after_trade
    percentage_knives = (knives_after_trade / total_silverware) * 100
    result = percentage_knives
    return result

print(solution())