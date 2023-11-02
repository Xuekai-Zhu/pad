def solution():
    """Josh went to the shopping center. He bought 9 films and 4 books. He also bought 6 CDs. Each film cost $5, each book cost $4 and each CD cost $3. How much did Josh spend in all?"""
    num_films = 9
    num_books = 4
    num_cds = 6
    cost_per_film = 5
    cost_per_book = 4
    cost_per_cd = 3
    total_cost = (num_films * cost_per_film) + (num_books * cost_per_book) + (num_cds * cost_per_cd)
    result = total_cost
    return result

print(solution())