def solution():
    """Kwame studied for the history test for 2.5 hours. Connor studied for 1.5 hours and Lexia studied for 97 minutes. How many minutes more did Kwame and Connor study than Lexia?"""
    kwame_study_time = 2.5 * 60
    connor_study_time = 1.5 * 60
    lexia_study_time = 97
    total_study_time = (kwame_study_time + connor_study_time) - lexia_study_time
    result = total_study_time
    return result

print(solution())