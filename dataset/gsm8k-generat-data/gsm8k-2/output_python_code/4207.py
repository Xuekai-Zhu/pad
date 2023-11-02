def solution():
    """A book is 98 pages long. Half of the pages are filled with images, and 11 with an introduction. Of the remaining pages, half are blank and the other half are filled with text. How many pages with text are there?"""
    total_pages = 98
    intro_pages = 11
    image_pages = total_pages / 2
    text_pages = (total_pages - intro_pages - image_pages) / 2
    result = text_pages
    return result

print(solution())