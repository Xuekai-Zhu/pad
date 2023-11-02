def solution():
    """Yvonne and Janna were writing their 1000-word pair research paper. Yvonne was able to write 400 words while Janna wrote 150 more words than Yvonne. When they edited their paper, they removed 20 words and added twice as many words as they removed. How many more words should they add to reach the research paper requirement?"""
    # Define the total word requirement for their research paper
    WORD_REQUIREMENT = 1000

    # Define the number of words Yvonne wrote and the number of words Janna wrote
    yvonne_words = 400
    janna_words = yvonne_words + 150

    # Calculate the total number of words before editing
    total_words = yvonne_words + janna_words

    # Calculate the number of words they removed and added during editing
    words_removed = 20
    words_added = words_removed * 2

    # Calculate the total number of words after editing
    total_words = total_words - words_removed + words_added

    # Calculate the number of words they still need to add to meet the requirement
    words_needed = WORD_REQUIREMENT - total_words

    # Display the number of words they need to add
    result = words_needed
    return result

print(solution())