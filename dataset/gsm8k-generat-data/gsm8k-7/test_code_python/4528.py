def solution():
    num_players = 16
    jersey_price = 25
    shorts_price = 15.2
    socks_price = 6.8

    # Calculate the total cost of all jerseys
    total_jersey_cost = num_players * jersey_price

    # Calculate the total cost of all shorts
    total_shorts_cost = num_players * shorts_price

    # Calculate the total cost of all socks
    total_socks_cost = num_players * socks_price

    # Calculate the total cost of all equipment for all players
    total_cost = total_jersey_cost + total_shorts_cost + total_socks_cost
    result = total_cost
    return result

print(solution())