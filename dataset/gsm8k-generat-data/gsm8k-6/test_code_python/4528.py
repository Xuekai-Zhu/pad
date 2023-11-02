def solution():
    # Calculate the total cost of equipment for 16 players
    jersey_cost = 25 * 16
    shorts_cost = 15.20 * 16
    socks_cost = 6.80 * 2 * 16  # each player needs one pair of socks
    total_cost = jersey_cost + shorts_cost + socks_cost
    result = total_cost
    return result

print(solution())