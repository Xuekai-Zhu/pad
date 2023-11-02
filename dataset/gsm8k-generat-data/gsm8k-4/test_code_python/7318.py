def solution():
    """Each purple book has 230 pages. Each orange book contains 510 pages. Mirella read 5 purple books and 4 orange books. How many more orange pages did she read than purple pages?"""
    # Define the number of pages per purple book and per orange book
    PURPLE_PAGES = 230
    ORANGE_PAGES = 510

    # Define the number of purple books and orange books read
    purple_books_read = 5
    orange_books_read = 4

    # Calculate the total number of purple and orange pages read
    total_purple_pages = purple_books_read * PURPLE_PAGES
    total_orange_pages = orange_books_read * ORANGE_PAGES

    # Calculate the difference between the total orange and purple pages read
    orange_pages_difference = total_orange_pages - total_purple_pages

    # Return the result
    result = orange_pages_difference
    return result

print(solution())