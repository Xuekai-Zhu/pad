def solution():
    
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