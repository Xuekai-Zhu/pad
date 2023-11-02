def solution():
    # Define the total number of pages and the number of pages with images and the introduction
    total_pages = 98
    pages_with_images = total_pages / 2
    pages_with_intro = 11

    # Calculate the number of pages without images or the intro
    pages_without_images_or_intro = total_pages - pages_with_images - pages_with_intro

    # Calculate the number of pages with text
    pages_with_text = pages_without_images_or_intro / 2
    result = pages_with_text
    return result

print(solution())