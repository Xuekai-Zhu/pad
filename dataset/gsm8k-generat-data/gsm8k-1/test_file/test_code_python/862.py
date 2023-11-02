def solution():
    """Together, Sofie, Anne, and Fawn have 85 books. If Sofie has 25 more books than Anne, and Anne has 12 fewer books than Fawn does, how many books does Fawn have?"""
    total_books = 85
    annes_books = (total_books - 25 - 12) / 3
    fawns_books = annes_books + 12
    result = fawns_books
    return result

print(solution())