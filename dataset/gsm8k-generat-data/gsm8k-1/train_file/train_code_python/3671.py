def solution():
    """Salem loves to write poems, and she always stores her poem in a creativity box kept safely in her home library. Last week, she created a poem with 20 stanzas. If each stanza has 10 lines, and each line has 8 words, calculate the total number of words in the poem."""
    stanzas = 20
    lines_per_stanza = 10
    words_per_line = 8
    total_words = stanzas * lines_per_stanza * words_per_line
    result = total_words
    return result

print(solution())