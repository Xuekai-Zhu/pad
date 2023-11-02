def solution():
    """Vinnie is writing an essay and needs to make sure that he has not exceeded the 1000-word limit. He wrote 450 words on Saturday and 650 words on Sunday. How many words has Vinnie exceeded the limit by?"""
    word_limit = 1000
    saturday_words = 450
    sunday_words = 650
    total_words = saturday_words + sunday_words
    exceeded_words = max(total_words - word_limit, 0)
    result = exceeded_words
    return result

print(solution())