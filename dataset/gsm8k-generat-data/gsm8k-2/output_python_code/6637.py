def solution():
    """Milton has some books about zoology and 4 times as many books about botany. If he has 80 books total, how many zoology books does he have?"""
    total_books = 80
    botany_books = total_books / 5
    zoology_books = total_books - botany_books
    result = zoology_books
    return result

print(solution())