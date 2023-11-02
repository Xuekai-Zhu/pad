def solution():
    johnny_ words = 150
    madeline_words = 2 * johnny_words
    timothy_words = madeline_words + 30
    words_per_page = 260
    johnny_pages = johnny_words / words_per_page
    madeline_pages = madeline_words / words_per_page
    timothy_pages = timothy_words / words_per_page
    total_pages = johnny_pages + madeline_pages + timothy_pages
    result = total_pages
    return result

print(solution())