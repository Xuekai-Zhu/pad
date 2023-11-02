def solution():
    """A book is 98 pages long. Half of the pages are filled with images, and 11 with an introduction. Of the remaining pages, half are blank and the other half are filled with text. How many pages with text are there?"""
    # Define the total number of pages
    total_pages = 98

    # Calculate the number of pages with images
    image_pages = total_pages / 2

    # Calculate the number of pages with introduction
    intro_pages = 11

    # Calculate the number of remaining pages
    remaining_pages = total_pages - image_pages - intro_pages

    # Calculate the number of pages with text
    text_pages = remaining_pages / 2

    # return the result
    result = text_pages
    return result

print(solution())