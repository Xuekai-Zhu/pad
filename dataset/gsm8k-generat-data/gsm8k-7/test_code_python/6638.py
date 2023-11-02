def solution():
    total_books = 80
    botany_books = total_books // 5  # Milton has 4 times as many botany books as zoology books
    zoology_books = total_books - botany_books
    result = zoology_books
    return result

print(solution())