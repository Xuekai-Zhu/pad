def solution():
    johnny_words = 150
    madeline_words = johnny_words * 2
    timothy_words = madeline_words + 30
    page_length = 260

    # Calculate the number of pages for each essay
    johnny_pages = johnny_words / page_length
    madeline_pages = madeline_words / page_length
    timothy_pages = timothy_words / page_length

    # Calculate the total number of pages for all three essays
    total_pages = johnny_pages + madeline_pages + timothy_pages
    result = total_pages
    return result

print(solution())