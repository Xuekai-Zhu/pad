def solution():
    total_pages = 98  # The book has 98 pages
    image_pages = total_pages / 2  # Half of the pages are filled with images
    intro_pages = 11  # 11 pages are used for the introduction
    remaining_pages = total_pages - image_pages - intro_pages  # Calculate the remaining pages

    # Calculate the number of pages filled with text
    text_pages = remaining_pages / 2
    result = text_pages
    return result

print(solution())