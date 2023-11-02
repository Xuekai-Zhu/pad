def solution():
    """Johnny wrote an essay with 150 words. Madeline wrote an essay that was double in length, and Timothy wrote an essay that had 30 words more than Madeline's. If one page contains 260 words, how many pages do Johnny, Madeline, and Timothy's essays fill?"""
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