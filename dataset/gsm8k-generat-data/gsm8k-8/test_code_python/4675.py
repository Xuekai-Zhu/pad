def solution():
    # Calculate the number of spoons Carolyn has
    num_knives = 6
    num_forks = 12
    num_spoons = num_knives * 3

    # Calculate the new number of knives and spoons after the trade
    num_knives_after_trade = num_knives + 10
    num_spoons_after_trade = num_spoons - 6

    # Calculate the total number of pieces of silverware Carolyn has
    total_silverware = num_knives + num_forks + num_spoons

    # Calculate the percentage of Carolyn's silverware that is knives
    percentage_knives = (num_knives_after_trade / total_silverware) * 100

    result = percentage_knives
    return result

print(solution())