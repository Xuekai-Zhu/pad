def solution():
    # Calculate the initial number of spoons and knives
    knives = 6
    forks = 12
    spoons = 3 * knives

    # Calculate the number of spoons and knives after the trade
    traded_knives = 10
    traded_spoons = 6
    knives += traded_knives
    spoons -= traded_spoons

    # Calculate the total number of pieces of silverware
    total_silverware = knives + forks + spoons

    # Calculate the percentage of knives
    percentage_knives = (knives / total_silverware) * 100
    result = percentage_knives
    return result

print(solution())