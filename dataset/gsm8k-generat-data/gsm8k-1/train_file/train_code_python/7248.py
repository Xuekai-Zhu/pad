def solution():
    """Vinnie is writing an essay and needs to make sure that he has not exceeded the 1000-word limit. He wrote 450 words on Saturday and 650 words on Sunday. How many words has Vinnie exceeded the limit by?"""
    word_limit = 1000
    words_on_saturday = 450
    words_on_sunday = 650
    total_words = words_on_saturday + words_on_sunday
    amount_exceeded = total_words - word_limit
    result = amount_exceeded
    return result

print(solution())