def solution():
    """Horatio is a poet composing sonnets for his lady fair. He believes it will take many of his sonnets to win her over. Each sonnet is fourteen lines long. His lady fair tells him to leave her alone after he reads her only seven sonnets, and Horatio is heartbroken over the 70 romantic lines he wrote that she never heard. How many sonnets did Horatio write in all?"""
    lines_per_sonnet = 14
    unheard_lines = 70
    total_lines = lines_per_sonnet * (7 + (unheard_lines / lines_per_sonnet))
    total_sonnets = total_lines / lines_per_sonnet
    result = total_sonnets
    return result

print(solution())