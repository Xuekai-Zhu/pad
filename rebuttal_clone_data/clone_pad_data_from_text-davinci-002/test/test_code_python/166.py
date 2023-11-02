def solution():
    books_wanted = 8
    cost_per_book = 5
    money_needed = books_wanted * cost_per_book
    money_saved = 13
    money_still_needed = money_needed - money_saved
    result = money_still_needed
    return result

print(solution())