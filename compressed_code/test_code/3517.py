def solution():
    
    num_players = 16
    jersey_cost = 25
    shorts_cost = 15.20
    socks_cost = 6.80
    total_cost_per_player = jersey_cost + shorts_cost + socks_cost
    total_cost = total_cost_per_player * num_players
    result = total_cost
    return result

print(solution())