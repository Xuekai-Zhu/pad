def solution():
     
     total_chapters_read = 10 + 1 + 2
     pages_read_in_chapter_eleven = 20
     total_pages_read = (total_chapters_read * 40) - (40 - pages_read_in_chapter_eleven)
     result = total_pages_read
     return result

print(solution())