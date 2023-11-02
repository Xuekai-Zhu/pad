def solution():
    """Shelby had $20 to take to the book fair. She bought one book for $8 and another for $4. She decided to buy as many $4 posters as she could with the money she had left. How many posters can she buy?"""
    money_left = 20 - 8 - 4
    poster_cost = 4
    posters_bought = money_left // poster_cost
    result = posters_bought
    return result

print(solution())