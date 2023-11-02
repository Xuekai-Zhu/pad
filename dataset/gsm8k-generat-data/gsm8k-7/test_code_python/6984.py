def solution():
    total_words = 1000
    yvonne_words = 400
    janna_words = yvonne_words + 150
    removed_words = 20
    added_words = removed_words * 2

    # Calculate the total words written before editing
    initial_words = yvonne_words + janna_words

    # Calculate the total words after editing
    final_words = initial_words - removed_words + added_words

    # Calculate the remaining words needed to reach the research paper requirement
    remaining_words = total_words - final_words
    result = remaining_words
    return result

print(solution())