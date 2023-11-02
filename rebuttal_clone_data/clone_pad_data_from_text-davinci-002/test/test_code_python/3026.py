def solution():
    books_on_shelf = 99
    books_in_boxes = 45
    books_in_room = 21
    books_on_coffee_table = 4
    books_in_kitchen = 18
    books_in_free_box = 12
    total_books = books_on_shelf - books_in_boxes - books_in_room - books_on_coffee_table - books_in_kitchen + books_in_free_box
    result = total_books
    return result

print(solution())