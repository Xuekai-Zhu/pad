def solution():
    total_pages = 98 # pages in the book
    image_pages = total_pages/2 # pages filled with images
    intro_pages = 11 # pages with an introduction
    remaining_pages = total_pages - image_pages - intro_pages # remaining pages
    text_pages = remaining_pages/2 # half of the remaining pages are filled with text
    result = text_pages
    return result

print(solution())