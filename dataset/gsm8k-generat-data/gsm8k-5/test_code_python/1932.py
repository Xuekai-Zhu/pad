def solution():
    cost_per_player = 40  # Each football team member must pay $40 to attend the party
    num_players = 60  # There are 60 players on the football team
    num_parties = 8  # The football team attends 8 parties in a year

    # Calculate the total amount of money collected in the 8 parties
    total_money_collected = cost_per_player * num_players * num_parties
    result = total_money_collected
    return result

print(solution())