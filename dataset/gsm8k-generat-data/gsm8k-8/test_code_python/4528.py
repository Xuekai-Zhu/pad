def solution():
    # Define the cost of each piece of equipment
    jersey_cost = 25
    shorts_cost = 15.20
    socks_cost = 6.80

    # Define the number of players on the team
    num_players = 16

    # Calculate the total cost of all the equipment
    total_cost = num_players * (jersey_cost + shorts_cost + socks_cost)
    result = total_cost
    return result

print(solution())