def solution():
    
    # Define the number of pages to the inch
    PAGES_PER_INCH = 100

    # Define the length of the book in inches
    INCH_TO_INCH = 1.5

    # Calculate the number of pages on each side of the book
    pages_per_side = PAGES_PER_INCH / 2

    # Calculate the total number of pages in the book
    total_pages = pages_per_side * 3 * INCH_TO_INCH

    # Display the total number of pages
    result = total_pages
    return result

print(solution())