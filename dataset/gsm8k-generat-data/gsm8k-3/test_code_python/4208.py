def solution():
    """A book is 98 pages long. Half of the pages are filled with images, and 11 with an introduction.
    Of the remaining pages, half are blank and the other half are filled with text. How many pages with text are there?"""
    # Define the total number of pages in the book
    total_pages = 98

    # Calculate the number of pages with images
    image_pages = total_pages / 2

    # Calculate the number of introduction pages
    intro_pages = 11

    # Calculate the number of pages without images or introduction
    remaining_pages = total_pages - image_pages - intro_pages

    # Calculate the number of pages with text
    text_pages = remaining_pages / 2

    # Display the number of pages with text
    result = text_pages
    return result

print(solution())