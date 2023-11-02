def solution():
    num_chapters_read_before_4 = 10
    pages_per_chapter = 40

    pages_read_in_chapter_11 = 20
    chapters_read_after_4 = 2

    # Calculate the total number of chapters read
    total_chapters_read = num_chapters_read_before_4 + chapters_read_after_4

    # Calculate the total number of pages read before 4 o'clock
    total_pages_before_4 = num_chapters_read_before_4 * pages_per_chapter

    # Calculate the total number of pages read after 4 o'clock
    total_pages_after_4 = (chapters_read_after_4 * pages_per_chapter) + pages_read_in_chapter_11

    # Calculate the total number of pages read altogether
    total_pages = total_pages_before_4 + total_pages_after_4
    result = total_pages
    return result

print(solution())