def solution():
    """Horatio is a poet composing sonnets for his lady fair. He believes it will take many of his sonnets to win her over. Each sonnet is fourteen lines long. His lady fair tells him to leave her alone after he reads her only seven sonnets, and Horatio is heartbroken over the 70 romantic lines he wrote that she never heard. How many sonnets did Horatio write in all?"""
    # Define the number of lines per sonnet
    LINES_PER_SONNET = 14

    # Define the number of lines read by his lady fair
    LINES_READ = 7 * LINES_PER_SONNET

    # Define the number of lines never read by his lady fair
    LINES_UNREAD = 70

    # Calculate the total number of lines written by Horatio
    total_lines = LINES_READ + LINES_UNREAD

    # Calculate the total number of sonnets by dividing the total number of lines by the number of lines per sonnet
    total_sonnets = total_lines / LINES_PER_SONNET

    result = total_sonnets
    return result

print(solution())