def solution():
    
    johnny_essay = 150
    madeline_essay = 2 * johnny_essay
    timothy_essay = madeline_essay + 30
    total_essay_words = johnny_essay + madeline_essay + timothy_essay
    total_pages = total_essay_words // 260
    if total_essay_words % 260 != 0:
        total_pages += 1
    result = total_pages
    return result

print(solution())