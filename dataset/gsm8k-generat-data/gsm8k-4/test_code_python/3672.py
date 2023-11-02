def solution():
    """Salem loves to write poems, and she always stores her poem in a creativity box kept safely in her home library. Last week, she created a poem with 20 stanzas. If each stanza has 10 lines, and each line has 8 words, calculate the total number of words in the poem."""
    # Define the number of stanzas, lines, and words per line
    num_stanzas = 20
    num_lines_per_stanza = 10
    num_words_per_line = 8

    # Calculate the total number of words in the poem
    num_words = num_stanzas * num_lines_per_stanza * num_words_per_line

    # return the result
    result = num_words
    return result

print(solution())