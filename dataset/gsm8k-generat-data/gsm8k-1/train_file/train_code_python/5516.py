def solution():
    """Kwame studied for the history test for 2.5 hours. Connor studied for 1.5 hours and Lexia studied for 97 minutes. How many minutes more did Kwame and Connor study than Lexia?"""
    kwame_hours = 2.5
    connor_hours = 1.5
    lexia_minutes = 97
    kwame_minutes = kwame_hours * 60
    connor_minutes = connor_hours * 60
    total_minutes = kwame_minutes + connor_minutes
    diff_minutes = total_minutes - lexia_minutes
    result = diff_minutes
    return result

print(solution())