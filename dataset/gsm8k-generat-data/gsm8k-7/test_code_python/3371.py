def solution():
    total_pages = 95
    num_chapters = 5

    # Calculate the difference in page numbers between chapters
    page_diff = 3

    # Calculate the sum of page numbers for all chapters
    sum_page_numbers = ((2 * total_pages) - (num_chapters * num_chapters * page_diff)) / (2 * num_chapters)

    # Calculate the number of pages in the first chapter
    first_chapter_pages = sum_page_numbers - ((num_chapters - 1) * page_diff)
    result = first_chapter_pages
    return result

print(solution())