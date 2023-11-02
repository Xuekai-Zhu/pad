def solution():
    stanzas = 20  # Salem created 20 stanzas in her poem
    lines_per_stanza = 10  # Each stanza has 10 lines
    words_per_line = 8  # Each line has 8 words

    # Calculate the total number of words in the poem
    total_words = stanzas * lines_per_stanza * words_per_line
    result = total_words
    return result

print(solution())