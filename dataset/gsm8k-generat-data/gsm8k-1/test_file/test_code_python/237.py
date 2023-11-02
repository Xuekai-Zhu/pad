def solution():
    """Dolly has two books. Pandora has one. If both Dolly and Pandora read each others' books as well as their own, how many books will they collectively read by the end?"""
    dolly_books = 2
    pandora_books = 1
    total_books = dolly_books + pandora_books + dolly_books + pandora_books
    result = total_books
    return result

print(solution())