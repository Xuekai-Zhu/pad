def solution():
    # Calculate the total number of books on the top section of the cart
    top_section_books = 12 + 8 + 4

    # Calculate the total number of books on the bottom section of the cart
    bottom_section_mystery_books = 0.5 * (top_section_books)  # half of the books on the bottom section were mystery books
    bottom_section_books = bottom_section_mystery_books + 5 + 6  # add the mystery, Western, and biography books together

    # Calculate the total number of books on the cart
    total_books = top_section_books + bottom_section_books
    result = total_books
    return result

print(solution())