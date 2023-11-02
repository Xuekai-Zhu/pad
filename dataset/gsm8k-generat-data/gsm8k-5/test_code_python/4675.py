def solution():
    knives = 6
    forks = 12
    spoons = 3 * knives
    total_silverware = knives + forks + spoons
    knives_after_trade = knives + 10
    spoons_after_trade = spoons - 6

    # Calculate the percentage of Carolyn's silverware that is knives
    percent_knives = (knives_after_trade / (knives_after_trade + forks + spoons_after_trade)) * 100
    result = percent_knives
    return result

print(solution())