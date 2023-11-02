def solution():
    """Yvonne and Janna were writing their 1000-word pair research paper. Yvonne was able to write 400 words while Janna wrote 150 more words than Yvonne. When they edited their paper, they removed 20 words and added twice as many words as they removed. How many more words should they add to reach the research paper requirement?"""
    total_words = 1000
    yvonne_words = 400
    janna_words = yvonne_words + 150
    initial_sum = yvonne_words + janna_words
    edited_sum = initial_sum - 20 + (2 * 20)
    words_needed = total_words - edited_sum
    result = words_needed
    return result

print(solution())