def solution():
    
    johnny_length = 150
    madeline_length = johnny_length * 2
    timothy_length = madeline_length + 30
    page_length = 260
    johnny_pages = johnny_length / page_length
    madeline_pages = madeline_length / page_length
    timothy_pages = timothy_length / page_length
    total_pages = johnny_pages + madeline_pages + timothy_pages
    
    result = total_pages
    return result

print(solution())