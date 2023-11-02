def solution():
    num_players = 16 # There are 16 players on the football team

    #Calculate the cost of one set of equipment
    cost_one_set = 25 + 15.20 + 6.80 # The cost of one jersey, one pair of shorts, and one pair of socks

    #Calculate the total cost of all the equipment for all the players on the team
    total_cost = num_players * cost_one_set
    result = total_cost
    return result

print(solution())