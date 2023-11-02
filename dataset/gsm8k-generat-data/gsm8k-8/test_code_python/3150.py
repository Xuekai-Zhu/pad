def solution():
    # Define the cost of the new PlayStation and the money Percy already has
    playstation_cost = 500
    birthday_money = 200
    christmas_money = 150
    total_money = birthday_money + christmas_money

    # Calculate the remaining amount of money needed
    remaining_money = playstation_cost - total_money

    # Calculate the number of games Percy needs to sell to reach his goal
    games_needed = int(remaining_money / 7.5)
    result = games_needed
    return result

print(solution())