def solution():
    """Yvonne and Janna were writing their 1000-word pair research paper. Yvonne was able to write 400 words while Janna wrote 150 more words than Yvonne. When they edited their paper, they removed 20 words and added twice as many words as they removed. How many more words should they add to reach the research paper requirement?"""
    yvonne_words = 400
    janna_words = yvonne_words + 150
    total_words = yvonne_words + janna_words
    edited_words = total_words - 20
    added_words = 2 * 20
    remaining_words = 1000 - edited_words
    more_words_needed = remaining_words - added_words
    result = more_words_needed
    return result

print(solution())