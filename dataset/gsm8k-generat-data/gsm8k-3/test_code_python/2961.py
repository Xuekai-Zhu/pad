def solution():
    """Jasmine wants to organize her books in order of most number of pages to least number of pages. Jasmine's longest book has 396 pages and her shortest book has one-fourth as many pages as the longest. If the book in the middle of her shelf has three times the number of pages of the shortest book, then how many pages does the middle book have?"""
    # Define the number of pages of the longest book
    longest_book = 396

    # Define the number of pages of the shortest book
    shortest_book = longest_book / 4

    # Define the number of pages of the middle book
    middle_book = shortest_book * 3

    # Display the number of pages of the middle book
    result = middle_book
    return result

print(solution())