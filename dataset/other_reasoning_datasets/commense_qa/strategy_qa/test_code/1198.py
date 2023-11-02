def solution():
    book_title = "Alice's Adventures in Wonderland"
    tobacco_use = "enjoyable"
    if tobacco_use in book_title:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())