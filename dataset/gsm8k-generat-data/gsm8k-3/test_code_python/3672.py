def solution():
    """Salem loves to write poems, and she always stores her poem in a creativity box kept safely in her home library. Last week, she created a poem with 20 stanzas. If each stanza has 10 lines, and each line has 8 words, calculate the total number of words in the poem."""
    # Define the number of stanzas, lines per stanza, and words per line
    STANZAS = 20
    LINES_PER_STANZA = 10
    WORDS_PER_LINE = 8

    # Calculate the total number of words in the poem
    total_words = STANZAS * LINES_PER_STANZA * WORDS_PER_LINE

    # Display the total number of words in the poem
    result = total_words
    return result

print(solution())