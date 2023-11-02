def solution():
    johnny_words = 150  # Johnny wrote an essay with 150 words
    madeline_words = 2 * johnny_words  # Madeline wrote an essay that was double in length
    timothy_words = madeline_words + 30  # Timothy wrote an essay that had 30 words more than Madeline's
    total_words = johnny_words + madeline_words + timothy_words  # Total words written

    pages = total_words / 260  # Calculate the number of pages

    result = pages
    return result

print(solution())