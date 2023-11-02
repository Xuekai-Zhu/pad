def solution():
    """Vinnie is writing an essay and needs to make sure that he has not exceeded the 1000-word limit. He wrote 450 words on Saturday and 650 words on Sunday. How many words has Vinnie exceeded the limit by?"""
    # Define the word limit and the number of words written
    WORD_LIMIT = 1000
    words_written = 450 + 650

    # Calculate the number of words exceeded the limit
    words_exceeded = max(0, words_written - WORD_LIMIT)

    # Return the result
    result = words_exceeded
    return result

print(solution())