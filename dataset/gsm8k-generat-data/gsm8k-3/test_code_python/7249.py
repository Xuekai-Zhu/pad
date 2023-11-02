def solution():
    """Vinnie is writing an essay and needs to make sure that he has not exceeded the 1000-word limit. He wrote 450 words on Saturday and 650 words on Sunday. How many words has Vinnie exceeded the limit by?"""
    # Define the essay word limit
    WORD_LIMIT = 1000

    # Calculate the total number of words Vinnie wrote
    total_words = 450 + 650

    # Calculate the number of words exceeded the limit
    exceed_words = max(total_words - WORD_LIMIT, 0)

    # Display the number of words exceeded the limit
    result = exceed_words
    return result

print(solution())