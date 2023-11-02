def solution():
    """Joe likes to play video games and he normally spends $50 a month on video games. Joe also sells his games for $30 each once he is done playing them. If he starts with $240, how many months can he buy games at $50 and sell them at $30 before he is out of money?"""
    game_cost = 50
    game_sale_price = 30
    starting_money = 240
    num_months = (starting_money // game_cost) + ((starting_money - (game_cost * (starting_money // game_cost))) // (game_cost - game_sale_price))
    result = num_months
    return result

print(solution())