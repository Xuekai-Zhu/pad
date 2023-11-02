def solution():
    """Joe likes to play video games and he normally spends $50 a month on video games. Joe also sells his games for $30 each once he is done playing them. If he starts with $240, how many months can he buy games at $50 and sell them at $30 before he is out of money?"""
    starting_money = 240
    cost_per_month = 50
    sell_price = 30
    number_of_games = 0
    num_months = 0

    while starting_money >= cost_per_month:
        starting_money -= cost_per_month
        number_of_games += 1
        starting_money += sell_price

        if number_of_games % 3 == 0:
            cost_per_month -= 10

        num_months += 1

    result = num_months
    return result

print(solution())