def solution():
    """Jasmine wants to organize her books in order of most number of pages to least number of pages. Jasmine's longest book has 396 pages and her shortest book has one-fourth as many pages as the longest. If the book in the middle of her shelf has three times the number of pages of the shortest book, then how many pages does the middle book have?"""
    longest_book = 396
    shortest_book = longest_book / 4
    middle_book = shortest_book * 3
    result = middle_book
    return result

print(solution())