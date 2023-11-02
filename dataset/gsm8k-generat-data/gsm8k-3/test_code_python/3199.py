def solution():
    """Horatio is a poet composing sonnets for his lady fair. He believes it will take many of his sonnets to win her over. Each sonnet is fourteen lines long. His lady fair tells him to leave her alone after he reads her only seven sonnets, and Horatio is heartbroken over the 70 romantic lines he wrote that she never heard. How many sonnets did Horatio write in all?"""
    # Define the number of lines per sonnet
    LINES_PER_SONNET = 14

    # Calculate the total number of lines Horatio wrote
    total_lines = LINES_PER_SONNET * (7 + (70/LINES_PER_SONNET))

    # Calculate the total number of sonnets Horatio wrote
    total_sonnets = int(total_lines / LINES_PER_SONNET)

    # Display the total number of sonnets
    result = total_sonnets
    return result

print(solution())