def solution():
    """Calculate the total number of pages that Mitchell had read altogether"""
    chapters_read_before_4 = 10
    pages_read_in_chapter_11 = 20
    chapters_read_after_4 = 2
    total_chapters_read = chapters_read_before_4 + chapters_read_after_4 + 1  # add 1 for chapter 11
    pages_per_chapter = 40
    total_pages_read = (total_chapters_read - 1) * pages_per_chapter + pages_read_in_chapter_11  # subtract 1 for chapter 11, which was partially read
    result = total_pages_read
    return result

print(solution())