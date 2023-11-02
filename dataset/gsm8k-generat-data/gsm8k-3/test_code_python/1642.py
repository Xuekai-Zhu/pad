def solution():
    """Johnny wrote an essay with 150 words. Madeline wrote an essay that was double in length, and Timothy wrote an essay that had 30 words more than Madeline's. If one page contains 260 words, how many pages do Johnny, Madeline, and Timothy's essays fill?"""
    # Define the number of words in Johnny's essay
    johnny_words = 150

    # Define the number of words in Madeline's essay
    madeline_words = 2 * johnny_words

    # Define the number of words in Timothy's essay
    timothy_words = madeline_words + 30

    # Calculate the total number of words
    total_words = johnny_words + madeline_words + timothy_words

    # Calculate the total number of pages
    total_pages = total_words // 260

    # Display the total number of pages
    result = total_pages
    return result

print(solution())