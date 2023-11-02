def solution():
    """Shelby had $20 to take to the book fair. She bought one book for $8 and another for $4. She decided to buy as many $4 posters as she could with the money she had left. How many posters can she buy?"""
    total_money = 20
    book1_price = 8
    book2_price = 4
    money_left = total_money - book1_price - book2_price
    poster_price = 4
    num_posters = money_left // poster_price
    result = num_posters
    return result

print(solution())