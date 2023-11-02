def solution():
    """Steve loves playing video games. His parents get him a console along with 5 games for his birthday. He saves up enough money to buy 1 game per month for a year, and then the following year he starts buying 2 games a month. For the third year, he buys 4 games a month as he has a new part-time job that makes him more money. He also gets 5 games for Christmas every year. How many games does Steve have after 3 years?"""
    starting_games = 5
    birthday_games = 5
    christmas_games = 15
    year_one_games = 12
    year_two_games = 24
    year_three_games = 48
    total_games = starting_games + birthday_games + christmas_games + year_one_games + year_two_games + year_three_games
    result = total_games
    return result

print(solution())