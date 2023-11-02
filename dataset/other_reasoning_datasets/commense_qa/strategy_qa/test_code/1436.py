def solution():
    holy_book = "Old Testament"
    acknowledged_books = ["Old Testament"]
    ten_commandments = True
    if holy_book not in acknowledged_books and ten_commandments:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())