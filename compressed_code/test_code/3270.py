def solution():
    
    total_pages = 98
    intro_pages = 11
    image_pages = total_pages / 2
    text_pages = (total_pages - intro_pages - image_pages) / 2
    result = text_pages
    return result

print(solution())