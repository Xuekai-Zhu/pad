def solution():

    books_in_library = 336
    books_taken_out = 124
    books_brought_back = 22
    books_now = books_in_library - books_taken_out + books_brought_back
    result = books_now
    return result

print(solution())