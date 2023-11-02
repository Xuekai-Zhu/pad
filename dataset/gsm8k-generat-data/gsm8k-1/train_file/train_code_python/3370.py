def solution():
    """Rita is reading a five-chapter book with 95 pages. Each chapter has three pages more than the previous one. How many pages does the first chapter have?"""
    total_pages = 95
    num_chapters = 5
    
    # equation for arithmetic sequence: a_n = a_1 + (n-1)d
    # where a_n is the nth term, a_1 is the first term, and d is the common difference
    
    common_diff = 3
    last_chapter = total_pages // num_chapters
    
    # solve for first chapter's pages: a_n = a_1 + (n-1)d -> a_1 = a_n - (n-1)d
    first_chapter = last_chapter - (num_chapters - 1) * common_diff
    
    result = first_chapter
    return result

print(solution())