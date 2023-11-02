def solution():
    """Yasna has two books. One book is 180 pages long, and the other book is 100 pages long. If Yasna wants to finish both of the books in two weeks, how many pages will Yasna need to read every day, if she reads an equal number of pages each day?"""
    # Define the number of pages in each book
    book1_pages = 180
    book2_pages = 100

    # Define the number of weeks Yasna has to finish the books
    weeks = 2

    # Calculate the total number of pages Yasna has to read
    total_pages = book1_pages + book2_pages

    # Calculate the number of pages Yasna has to read every day
    pages_per_day = total_pages / (weeks * 7)

    # Round up to the nearest integer
    pages_per_day = int(math.ceil(pages_per_day))

    # Return the result
    result = pages_per_day
    return result

print(solution())