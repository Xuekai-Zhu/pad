def solution():
    num_games_sold = 40
    price_per_game = 5

    # Calculate the total amount of money Zachary received
    zachary_money = num_games_sold * price_per_game

    # Calculate the amount of money Jason received (30% more than Zachary's money)
    jason_money = zachary_money * 1.3

    # Calculate the amount of money Ryan received ($50 more than Jason's money)
    ryan_money = jason_money + 50

    # Calculate the total amount of money the three friends received
    total_money = zachary_money + jason_money + ryan_money
    result = total_money
    return result

print(solution())