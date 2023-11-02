def solution():
    num_stanzas = 20
    num_lines_per_stanza = 10
    num_words_per_line = 8

    # Calculate the total number of lines in the poem
    total_lines = num_stanzas * num_lines_per_stanza

    # Calculate the total number of words in the poem
    total_words = total_lines * num_words_per_line
    result = total_words
    return result

print(solution())