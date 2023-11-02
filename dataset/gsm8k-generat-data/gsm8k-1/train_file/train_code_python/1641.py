def solution():
    """Johnny wrote an essay with 150 words. Madeline wrote an essay that was double in length, and Timothy wrote an essay that had 30 words more than Madeline's. If one page contains 260 words, how many pages do Johnny, Madeline, and Timothy's essays fill?"""
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