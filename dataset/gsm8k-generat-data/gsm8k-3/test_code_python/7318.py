def solution():
    """Each purple book has 230 pages. Each orange book contains 510 pages. Mirella read 5 purple books and 4 orange books. How many more orange pages did she read than purple pages?"""
    # Define the number of pages in each purple and orange book
    PURPLE_PAGES = 230
    ORANGE_PAGES = 510

    # Define the number of purple and orange books read
    purple_books = 5
    orange_books = 4

    # Calculate the total number of purple and orange pages read
    purple_pages = purple_books * PURPLE_PAGES
    orange_pages = orange_books * ORANGE_PAGES

    # Calculate the difference in the number of orange and purple pages read
    difference = orange_pages - purple_pages

    # Display the difference in the number of orange and purple pages read
    result = difference
    return result

print(solution())