def solution():
    """Rita is reading a five-chapter book with 95 pages. Each chapter has three pages more than the previous one. How many pages does the first chapter have?"""
    total_pages = 95
    num_chapters = 5
    first_chapter_pages = (total_pages - (num_chapters * 3)) / ((num_chapters * 2) - 1)
    result = first_chapter_pages
    return result

print(solution())