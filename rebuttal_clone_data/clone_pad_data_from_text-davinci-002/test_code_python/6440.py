def solution():
    number_of_players = 12
    cost_of_shirt = 7.50
    discounted_cost_of_shirt = 6.75
    cost_of_pants = 15.00
    discounted_cost_of_pants = 13.50
    cost_of_socks = 4.50
    discounted_cost_of_socks = 3.75
    cost_of_uniform = cost_of_shirt + cost_of_pants + cost_of_socks
    discounted_cost_of_uniform = discounted_cost_of_shirt + discounted_cost_of_pants + discounted_cost_of_socks
    savings = (cost_of_uniform - discounted_cost_of_uniform) * number_of_players
    result = savings

    return result

print(solution())