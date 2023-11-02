def solution():
    """Raul had $87 to spare so he decided to go to the bookshop. Raul bought 8 comics, each of which cost $4. How much money does Raul have left?"""
    initial_money = 87
    num_comics = 8
    comic_cost = 4
    total_cost = num_comics * comic_cost
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())