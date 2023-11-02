def solution():
    """Four books are arranged on a shelf. The first book is 31 mm thick while the second book is 50 mm thick. The third book is 5 mm less thick than the second book, and the fourth book is twice as thick as the first book. What is the total thickness of the four books?"""
    first_book_thickness = 31
    second_book_thickness = 50
    third_book_thickness = second_book_thickness - 5
    fourth_book_thickness = 2 * first_book_thickness
    total_thickness = first_book_thickness + second_book_thickness + third_book_thickness + fourth_book_thickness
    result = total_thickness
    return result

print(solution())