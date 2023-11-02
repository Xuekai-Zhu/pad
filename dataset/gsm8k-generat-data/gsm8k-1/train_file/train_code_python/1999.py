def solution():
    """Tara is saving up to buy a new clarinet. She already has $10 saved. The clarinet costs $90. She plans to sell her old books to make the money. She sells each book of hers for $5. However, when she is halfway towards her goal, she loses all her savings and has to start over. How many books does she sell in total by the time she reaches her goal?"""
    savings = 10
    goal = 90
    books_per_goal = (goal - savings) / 5
    total_books = books_per_goal * 2
    result = total_books
    return result

print(solution())