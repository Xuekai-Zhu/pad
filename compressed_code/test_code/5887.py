def solution():
    
    chapters_read_before_4 = 10
    pages_read_in_chapter_11 = 20
    chapters_read_after_4 = 2
    total_chapters_read = chapters_read_before_4 + chapters_read_after_4 + 1  
    pages_per_chapter = 40
    total_pages_read = (total_chapters_read - 1) * pages_per_chapter + pages_read_in_chapter_11  
    result = total_pages_read
    return result

print(solution())