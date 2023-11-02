def solution():

    fiction_books = 5 
    nonfiction_books = fiction_books + 4
    autobiographies = fiction_books * 2
    picture_books = 35 - fiction_books - nonfiction_books - autobiographies
    result = picture_books
    return result

print(solution())