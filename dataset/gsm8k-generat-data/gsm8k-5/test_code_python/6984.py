def solution():
    total_words = 1000
    yvonne_words = 400
    janna_words = yvonne_words + 150
    initial_total_words = yvonne_words + janna_words

    # Editing process
    edited_total_words = initial_total_words - 20
    edited_total_words += 2 * 20  # Added twice as many words as they removed

    # Calculate how many more words they need to reach the research paper requirement
    remaining_words = total_words - edited_total_words
    result = remaining_words
    return result

print(solution())