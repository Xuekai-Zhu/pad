def solution():
    """Yvonne and Janna were writing their 1000-word pair research paper. Yvonne was able to write 400 words while Janna wrote 150 more words than Yvonne. When they edited their paper, they removed 20 words and added twice as many words as they removed. How many more words should they add to reach the research paper requirement?"""
    # Define the total required words for the research paper
    required_words = 1000

    # Calculate the total words written by Yvonne and Janna
    yvonne_words = 400
    janna_words = yvonne_words + 150

    total_words = yvonne_words + janna_words

    # Calculate the net change in words after editing
    net_change = 2 * 20 - 20

    # Calculate the current total words after editing
    current_words = total_words + net_change

    # Calculate the remaining words needed to meet the requirement
    remaining_words = required_words - current_words

    result = remaining_words
    return result

print(solution())