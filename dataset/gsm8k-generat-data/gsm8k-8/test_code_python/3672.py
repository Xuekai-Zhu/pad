def solution():
    # Define the number of stanzas and lines per stanza
    num_stanzas = 20
    lines_per_stanza = 10

    # Define the number of words per line
    words_per_line = 8

    # Calculate the total number of words in the poem
    total_words = num_stanzas * lines_per_stanza * words_per_line
    result = total_words
    return result

print(solution())