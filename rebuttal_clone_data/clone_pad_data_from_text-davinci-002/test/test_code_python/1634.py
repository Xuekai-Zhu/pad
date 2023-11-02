def solution():
    savings_june = 27
    savings_july = 14
    savings_august = 21
    spent_books = 5
    spent_shoes = 17
    total_saved = savings_june + savings_july + savings_august
    total_spent = spent_books + spent_shoes
    money_left = total_saved - total_spent
    result = money_left
    return result

print(solution())